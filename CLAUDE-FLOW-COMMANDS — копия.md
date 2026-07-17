# Claude-Flow Commands Reference

## Global (works from any directory)
claude-flow --version
claude-flow --help

## Local (must be in project directory)
cd D:\Users\NIKITA\Documents\DEV\katana-vectorbt
claude-flow status
claude-flow agent list
claude-flow agent spawn -t researcher
claude-flow agent spawn -t coder

## Swarm Commands
claude-flow swarm init
claude-flow swarm status

## Memory Commands
claude-flow memory init
claude-flow memory search -q "search term"

## Daemon Commands
claude-flow daemon start
claude-flow daemon stop

## MCP Server
claude-flow mcp start
claude-flow mcp status
