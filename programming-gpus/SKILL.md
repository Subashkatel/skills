---
name: programming-gpus
description: "Guides GPU programming and optimization for CUDA, HIP, SYCL, Triton, OpenCL, renderers, and scientific kernels with profiling and correctness evidence."
---

# Programming GPUs

## Rule

Correctness first, baseline second, profiling third, optimization fourth. Do not claim speedups, bottlenecks, or occupancy improvements without measurement or clearly marking them as hypotheses.

## Workflow

1. Identify target stack: CUDA, HIP/ROCm, SYCL, Triton, OpenCL, vendor, GPU model, driver/toolkit, compiler flags, and operating system.
2. Establish correctness:
   - CPU or trusted reference implementation.
   - Input ranges and edge cases.
   - Numerical precision and tolerance.
   - Determinism requirements.
3. Establish a benchmark protocol:
   - Warmup.
   - Synchronization.
   - Repeated runs.
   - Representative problem sizes.
   - Timing method.
4. Profile before optimizing:
   - Kernel time and launch overhead.
   - Host/device transfer time.
   - Memory bandwidth and coalescing.
   - Occupancy and register/shared-memory limits.
   - Divergence and instruction mix.
5. Pick one bottleneck hypothesis and one intervention at a time.
6. Re-run correctness and benchmark after each change.
7. Record evidence in `templates/gpu-performance-report.md`.

## Optimization checklist

Use `reference/gpu-optimization-checklist.md` for detailed checks. Common categories:

- Data layout and coalesced global memory access.
- Shared memory/LDS reuse and bank conflicts.
- Register pressure and occupancy.
- Warp/wavefront divergence.
- Arithmetic intensity and roofline position.
- Asynchronous copy/overlap when appropriate.
- Kernel fusion or splitting based on evidence.
- Portability differences between NVIDIA and AMD.

## Tools

Use available local tools only. If a profiler or GPU stack is unavailable, say so and provide the exact commands the user can run.

- CUDA: Nsight Compute, Nsight Systems, nvprof legacy, cuda events, nvidia-smi.
- ROCm/HIP: rocprofv3, ROCprof Compute Viewer, rocm-smi.
- General: build logs, compiler resource usage, benchmark scripts.

## Scripts

- `scripts/gpu_env_probe.py` prints available GPU/profiler commands.
- `scripts/repeat_command.py` can run a command repeatedly and report simple timing statistics.

## Performance simplification gate

Before adding a new kernel, abstraction, cache, or runtime path, apply `approximating-changes`: remove work first, do setup once, reduce launches or transfers, constrain shapes/layouts, and only approximate with an explicit tolerance plus benchmark and correctness evidence.

## GPU readability rules

GPU code may be low-level, but it must still be readable. Prefer names such as `thread_index_x`, `block_index`, `element_index`, `row_index`, `column_index`, `shared_memory_tile`, `launch_configuration`, `input_stride`, and `output_stride` over unexplained abbreviations. If a dense expression or compact indexing pattern is required for performance, isolate it, measure it, and add a short comment explaining the memory-layout or hardware reason.
