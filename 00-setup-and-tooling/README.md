# 🛠️ Phase 00: Setup and Tooling

This phase focuses on configuring a bulletproof, reproducible AI development environment. Before writing math or model code, the system, package managers, runtimes, and hardware acceleration layers must be completely aligned.

---

## 🎯 Objectives
- **Toolchain Installation:** Set up Python 3.11+, Node.js 20+, and Rust compilation toolchains from scratch.
- **Reproducibility:** Configure virtual environments and modern package managers for stable, deterministic environments.
- **Hardware Acceleration:** Verify compute/GPU acceleration access via CUDA (Nvidia) or MPS (Apple Silicon) using a native tensor baseline test.
- **Architecture Literacy:** Master the four-layer engineering stack underpinning modern AI infrastructure.

---

## 🗂️ The Four-Layer AI Stack
Understanding how code interacts with hardware is crucial for optimization:

1. **System Layer:** Hardware architecture, OS, drivers, and compute platforms (e.g., CPU, GPU, CUDA, MPS).
2. **Packages Layer:** Package managers that isolate dependencies and resolve reproducible builds (e.g., `uv`, `pnpm`, `cargo`).
3. **Runtimes Layer:** Execution engines and language environments (e.g., Python Interpreter, Node.js V8 Engine, Rust Binary Compiler).
4. **AI Libraries Layer:** High-level frameworks that orchestrate model workflows and computational graphs (e.g., PyTorch, NumPy).

---

## 💻 Language & Toolchain Ecosystem

| Language | Used In | Package Manager |
| :--- | :--- | :--- |
| **Python** | Phases 1-12 (ML, DL, NLP, Vision, Audio, LLMs) | `uv` |
| **TypeScript** | Phases 13-17 (Tools, Agents, Swarms, Infra) | `pnpm` |
| **Rust** | Phases 12, 15-17 (Performance-critical systems) | `cargo` |
| **Julia** | Phase 1 (Math foundations) | `Pkg` |

---

## 📜 Verification & Artifacts
*Add logs, scripts, or outputs proving your configurations are functional here.*

- [ ] Python, Node.js, Rust, and Julia installation outputs.
- [ ] PyTorch/TensorFlow script showing active GPU/CUDA acceleration.
- [ ] Shared configuration files (e.g., system paths, global settings).
