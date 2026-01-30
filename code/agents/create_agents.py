#!/usr/bin/env python3
"""
從 YAML 配置文件批量創建所有 Agent

使用方式:
    python create_agents.py
    python create_agents.py --config-dir ./code/agents
    python create_agents.py --dry-run
"""

import os
import sys
import yaml
import argparse
from typing import Dict, List, Any, Optional

# 模擬 Nebula API (實際使用時應從 nebula import manage_agents)
def manage_agents(**kwargs):
    """
    模擬的 manage_agents 函數
    實際使用時應替換為: from nebula import manage_agents
    """
    action = kwargs.get('action')
    if action == 'create':
        return {
            'success': True,
            'agent_id': f"agt_simulated_{kwargs.get('name', 'unknown').replace(' ', '_')}",
            'name': kwargs.get('name'),
            'description': kwargs.get('description')
        }
    return {'success': False}


class AgentCreator:
    """從配置文件創建 Agent 的工具類"""
    
    def __init__(self, config_dir: str = 'code/agents', dry_run: bool = False):
        self.config_dir = config_dir
        self.dry_run = dry_run
        self.created_agents = []
        self.failed_agents = []
    
    def load_config(self, config_path: str) -> Optional[Dict]:
        """載入單個 YAML 配置文件"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            return config
        except Exception as e:
            print(f"❌ Failed to load {config_path}: {e}")
            return None
    
    def extract_toolkits(self, config: Dict) -> List[str]:
        """從配置提取工具包清單"""
        tools = config.get('available_tools', [])
        toolkits = set()
        
        for tool in tools:
            if isinstance(tool, dict):
                tool_name = tool.get('tool', tool.get('tool_name', ''))
                
                # 映射工具到工具包
                if any(keyword in tool_name.lower() for keyword in ['web', 'search', 'scrape', 'extract']):
                    toolkits.add('Web')
                if any(keyword in tool_name.lower() for keyword in ['python', 'execution', 'code']):
                    toolkits.add('Python')
                if 'api' in tool_name.lower():
                    toolkits.add('API')
        
        return list(toolkits)
    
    def extract_prompt_sections(self, config: Dict) -> Dict[str, Any]:
        """從配置提取 prompt sections"""
        metadata = config.get('agent_metadata', {})
        capabilities = config.get('core_capabilities', [])
        workflow = config.get('workflow', {})
        
        # 處理 capabilities
        cap_list = []
        if isinstance(capabilities, list):
            for cap in capabilities:
                if isinstance(cap, dict):
                    cap_list.append(cap.get('name', str(cap)))
                else:
                    cap_list.append(str(cap))
        
        return {
            'identity': metadata.get('role', metadata.get('name', '')),
            'purpose': metadata.get('description', ''),
            'capabilities': cap_list,
            'workflow': self._format_workflow(workflow),
            'best_practices': self._extract_best_practices(config)
        }
    
    def _format_workflow(self, workflow: Dict) -> str:
        """格式化工作流程為字串"""
        if not workflow:
            return ""
        
        workflow_text = []
        for step_key in sorted(workflow.keys()):
            step = workflow[step_key]
            if isinstance(step, dict):
                workflow_text.append(
                    f"{step.get('name', step_key)}: {step.get('process', '')}"
                )
        
        return "\n".join(workflow_text)
    
    def _extract_best_practices(self, config: Dict) -> List[str]:
        """提取最佳實踐"""
        quality = config.get('quality_standards', {})
        practices = []
        
        for key, value in quality.items():
            practices.append(f"{key}: {value}")
        
        return practices
    
    def create_agent_from_config(self, config_path: str) -> Optional[Dict]:
        """從配置文件創建單個 Agent"""
        
        # 載入配置
        config = self.load_config(config_path)
        if not config:
            return None
        
        metadata = config.get('agent_metadata', {})
        name = metadata.get('name', 'Unnamed Agent')
        description = metadata.get('description', '')
        
        print(f"\n{'='*60}")
        print(f"📝 Creating Agent: {name}")
        print(f"{'='*60}")
        
        if self.dry_run:
            print("🔍 DRY RUN MODE - Not actually creating agent")
            print(f"  Name: {name}")
            print(f"  Description: {description[:100]}...")
            print(f"  Toolkits: {self.extract_toolkits(config)}")
            return {
                'dry_run': True,
                'name': name,
                'config_path': config_path
            }
        
        try:
            # 提取配置資訊
            toolkits = self.extract_toolkits(config)
            prompt_sections = self.extract_prompt_sections(config)
            
            # 創建 Agent
            result = manage_agents(
                action='create',
                name=name,
                description=description,
                prompt_sections=prompt_sections,
                selected_toolkits=toolkits
            )
            
            if result.get('success'):
                print(f"✅ Successfully created: {name}")
                print(f"   Agent ID: {result.get('agent_id')}")
                print(f"   Toolkits: {', '.join(toolkits)}")
                
                self.created_agents.append({
                    'name': name,
                    'agent_id': result.get('agent_id'),
                    'config_path': config_path
                })
                
                return result
            else:
                print(f"❌ Failed to create: {name}")
                self.failed_agents.append({
                    'name': name,
                    'config_path': config_path,
                    'error': result.get('error', 'Unknown error')
                })
                return None
                
        except Exception as e:
            print(f"❌ Exception while creating {name}: {e}")
            self.failed_agents.append({
                'name': name,
                'config_path': config_path,
                'error': str(e)
            })
            return None
    
    def create_all_agents(self) -> Dict[str, List]:
        """批量創建所有 Agent"""
        
        print(f"\n🚀 Starting Agent Creation Process")
        print(f"📁 Config Directory: {self.config_dir}")
        print(f"🔍 Dry Run: {self.dry_run}")
        
        # 尋找所有配置文件
        config_files = []
        for file in os.listdir(self.config_dir):
            if file.startswith('agent_') and file.endswith('.yaml'):
                config_files.append(os.path.join(self.config_dir, file))
        
        print(f"📋 Found {len(config_files)} configuration files")
        
        # 創建順序：主控 Agent 最後創建
        orchestrator_config = None
        other_configs = []
        
        for config_file in config_files:
            if 'orchestrator' in config_file:
                orchestrator_config = config_file
            else:
                other_configs.append(config_file)
        
        # 先創建子 Agent
        for config_file in other_configs:
            self.create_agent_from_config(config_file)
        
        # 最後創建主控 Agent
        if orchestrator_config:
            self.create_agent_from_config(orchestrator_config)
        
        # 顯示總結
        self.print_summary()
        
        return {
            'created': self.created_agents,
            'failed': self.failed_agents
        }
    
    def print_summary(self):
        """列印創建總結"""
        
        print(f"\n{'='*60}")
        print(f"📊 Creation Summary")
        print(f"{'='*60}")
        
        print(f"\n✅ Successfully Created: {len(self.created_agents)}")
        for agent in self.created_agents:
            print(f"   • {agent['name']}")
            if not self.dry_run:
                print(f"     ID: {agent['agent_id']}")
        
        if self.failed_agents:
            print(f"\n❌ Failed: {len(self.failed_agents)}")
            for agent in self.failed_agents:
                print(f"   • {agent['name']}")
                print(f"     Error: {agent['error']}")
        
        print(f"\n{'='*60}")
        
        if not self.dry_run:
            self.save_agent_mapping()
    
    def save_agent_mapping(self):
        """保存 Agent ID 映射到文件"""
        
        mapping_file = 'agent_id_mapping.yaml'
        mapping = {
            'created_at': __import__('datetime').datetime.now().isoformat(),
            'agents': {}
        }
        
        for agent in self.created_agents:
            mapping['agents'][agent['name']] = {
                'agent_id': agent['agent_id'],
                'config_path': agent['config_path']
            }
        
        with open(mapping_file, 'w', encoding='utf-8') as f:
            yaml.dump(mapping, f, allow_unicode=True)
        
        print(f"\n💾 Agent ID mapping saved to: {mapping_file}")


def main():
    """主函數"""
    
    parser = argparse.ArgumentParser(
        description='從 YAML 配置文件創建 AI Agents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  python create_agents.py                           # 創建所有 Agent
  python create_agents.py --config-dir ./configs    # 指定配置目錄
  python create_agents.py --dry-run                 # 預覽但不實際創建
        """
    )
    
    parser.add_argument(
        '--config-dir',
        type=str,
        default='code/agents',
        help='配置文件目錄 (預設: code/agents)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='預覽模式，不實際創建 Agent'
    )
    
    args = parser.parse_args()
    
    # 檢查目錄是否存在
    if not os.path.isdir(args.config_dir):
        print(f"❌ Error: Directory not found: {args.config_dir}")
        sys.exit(1)
    
    # 創建 Agent
    creator = AgentCreator(
        config_dir=args.config_dir,
        dry_run=args.dry_run
    )
    
    results = creator.create_all_agents()
    
    # 返回狀態碼
    if results['failed']:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
