# Renderer Checklist

## Ownership
- Device/shell
- Pass graph
- Camera/projection
- Depth convention
- Resource layouts
- Shader contracts
- Capability handling

## Verification
- Console/GPU validation logs
- Actual PNG/GIF capture
- Crops for small features
- Semantic probes for anchors/counts/state
- Hardware profiler evidence for performance claims

## Failure smells
- Healthy stats, blank pixels
- Duplicated projection/depth constants
- Unowned time or randomness
- Fallback path hiding production renderer failure
