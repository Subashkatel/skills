---
name: debugging-gpu-renderers
description: "Debugs GPU renderers and scientific visualizations with shader, resource-layout, pass-order, depth, capability, and rendered-output evidence."
---

# Debugging GPU Renderers

Use this when correctness depends on GPU resource ownership, pass orchestration, shader contracts, depth semantics, or visual output.

## Workflow

1. **Inspect current owners.** Find device setup, pass graph, pipeline layouts, bind groups, shader contracts, camera/projection owner, depth convention, capability handling, and validation routes before changing anything.
2. **Define resources first.** Buffers, textures, uniforms, storage layouts, bind groups, update frequency, read/write access, lifetime, alignment, and ownership should be explicit before code changes.
3. **Choose the phase deliberately.** Use compute for parallel preparation, simulation, reductions, compaction, and work lists. Use render passes for rasterized output. Split phases when visibility or depth semantics differ.
4. **Single-source shared contracts.** Camera layouts, projection helpers, depth modes, frame phases, vertex strides, bind-group schemas, and semantic roles should have one owner consumed by renderers, shaders, and verifiers.
5. **Make validation visual and semantic.** Route stats, instance counts, or command success are not proof that pixels are right. Inspect actual captures and pair them with semantic probes.
6. **Profile separately from correctness.** Software fallback renderers or headless paths can be correctness proxies but are not performance oracles.
7. **Record evidence.** Save commands, captures, crops, profiler output, warnings, device info, and acceptance notes in the active spec or verification report.

## Rules

- Depth is a contract: compare mode, clear value, attachment format, pass order, and pipeline state move together.
- All pipelines in one render pass must be compatible with its attachments.
- Do not mix translucent overlays into depth-writing opaque geometry unless the phase explicitly owns that policy.
- Uniform and storage structs must respect alignment. Prefer obvious packing when it reduces ambiguity.
- WGSL or shader validation warnings are failed renders until explained.
- Stats that count submitted instances are not proof that content reached the frame.
- If a visual change touches camera, lighting, model geometry, resource layout, and pass order at once, split it so cause is observable.
- Frozen snapshots require owned time and seeded randomness; unowned clocks create flaky gates.
- Capability fallbacks must match product requirements. Do not silently route production visuals through unrelated fallback code to hide missing GPU behavior.

## Common failure smells

- Canvas is black or blank while app state looks healthy.
- A private projection helper appears beside a shared one.
- Verifier copies renderer constants by hand.
- A screenshot is mostly empty while counts are healthy.
- Labels, overlays, or world-space markers use screen-space hacks instead of semantic anchors.
- A baseline changed but nobody inspected the candidate image.
- Performance improved on fallback or tiny fixtures only.

## Done

A renderer change is done when resource contracts have one owner, validation warnings are resolved, actual captures are inspected, semantic probes agree with pixels, and performance claims use real hardware evidence when performance is claimed.
