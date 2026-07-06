# GPU optimization checklist

## Correctness
- Reference implementation exists.
- CPU/GPU results compared with justified tolerance.
- Edge cases tested: empty, tiny, non-multiple block sizes, large sizes, NaN/Inf if relevant.
- Floating-point order changes are expected and documented.

## Benchmarking
- Warmup runs performed.
- Device synchronization included around timing.
- Multiple repetitions with median/min/max.
- Representative problem sizes.
- Build type and compiler flags recorded.

## Memory
- Global memory accesses coalesced where possible.
- Strided or scattered accesses justified.
- Host/device transfers minimized or overlapped.
- Shared memory/LDS used for reuse, not by default.
- Bank conflicts checked when using tiled shared memory.

## Execution
- Block size justified experimentally.
- Occupancy limited by registers/shared memory only when measured.
- Divergence minimized in hot paths.
- Atomics reduced or aggregated when costly.
- Kernel launch overhead considered for tiny kernels.

## Portability
- Vendor-specific intrinsics isolated.
- Warp size assumptions documented.
- CUDA/HIP/SYCL/Triton version recorded.
- Fallback path or build guard exists when needed.
