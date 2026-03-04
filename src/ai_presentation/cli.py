"""Command-line interface for AI Presentation System."""

import argparse
import asyncio
import logging
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ai_presentation.orchestrator import PresentationOrchestrator  # noqa: E402

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="AI Presentation System - 8-agent collaboration"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate a presentation")
    generate_parser.add_argument("--topic", required=True, help="Presentation topic")
    generate_parser.add_argument(
        "--output", default="output.pptx", help="Output file path"
    )

    # Version command
    subparsers.add_parser("version", help="Show version")

    args = parser.parse_args()

    if args.command == "generate":
        asyncio.run(generate_presentation(args.topic, args.output))
    elif args.command == "version":
        print("AI Presentation System v2.0.0")
    else:
        parser.print_help()


async def generate_presentation(topic: str, output: str):
    """Generate presentation asynchronously."""
    logger.info(f"Generating presentation for topic: {topic}")
    orchestrator = PresentationOrchestrator()
    result = await orchestrator.generate_presentation(
        {
            "topic": topic,
            "scenario": {"topic": topic},
            "content": {"topic": topic},
        }
    )
    logger.info(f"Presentation saved to {output}")
    return result


if __name__ == "__main__":
    main()
