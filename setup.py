"""Setup configuration for AI Presentation System."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
      long_description = fh.read()

setup(
      name="ai-presentation-system",
      version="1.0.0",
      author="Glen Chen",
      author_email="glen200392@example.com",
      description="AI-powered presentation generation system with 6-agent collaboration",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/glen200392/ai-presentation-system",
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      classifiers=[
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Programming Language :: Python :: 3.10",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
      ],
      python_requires=">=3.8",
      install_requires=[
                "fastapi>=0.68.0",
                "uvicorn[standard]>=0.15.0",
                "pydantic>=1.8.0",
                "python-dotenv>=0.19.0",
                "aiohttp>=3.8.0",
                "pptx>=0.6.21",
                "requests>=2.26.0",
                "async-timeout>=3.0.0",
      ],
      extras_require={
                "dev": [
                              "pytest>=6.2.0",
                              "pytest-asyncio>=0.15.0",
                              "black>=21.0",
                              "flake8>=3.9.0",
                ],
      },
      entry_points={
                "console_scripts": [
                              "ai-presentation=ai_presentation.cli:main",
                ],
      },
)
