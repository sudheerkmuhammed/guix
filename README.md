# The Joy of Guix: Or How I Learned to Stop Worrying and Love the Parentheses

<div align="center">
  <img src="images/book_cover.jpg" width="480" alt="The Joy of Guix Book Cover"/>
  <br/><br/>
  <h3>A Practical, Sarcastic, and Deeply Technical Guide to Functional Computing</h3>
  <p>
    <strong>Author:</strong> Sudheer K. Mohammed &nbsp;|&nbsp;
    <strong>License:</strong> GNU General Public License v3 or later
  </p>
  <p>
    <a href="main.pdf"><strong>📥 Download PDF Edition</strong></a> &nbsp;•&nbsp;
    <a href="the_joy_of_guix.epub"><strong>📱 Download EPUB Edition</strong></a> &nbsp;•&nbsp;
    <a href="#-table-of-contents"><strong>📖 Read Online Below</strong></a>
  </p>
</div>

---

## 🧭 About This Book

Welcome to **The Joy of Guix**! This book is written for developers, systems engineers, DevOps practitioners, scientific researchers, and curious tinkerers who are exhausted by the fragility of traditional mutable operating systems and package managers.

Whether you run Guix as an unprivileged, transactional package manager on top of an existing distribution (**Ubuntu, Debian, Fedora, Arch, openSUSE**), or deploy it as a fully unified declarative operating system (**Guix System**), this book provides a complete, hands-on path from first principles to advanced mastery.

---

## 📑 Table of Contents

- [**Dedication & Colophon**](#dedication)
- [**Preface: The Imperative Hellscape and the Functional Cure**](#preface-the-imperative-hellscape-and-the-functional-cure)
- [**Part I: The Grand Illusion — Package Management Done Right**](#part-i-the-grand-illusion--package-management-done-right)
  - [Chapter 1: The Curse of FHS and the Salvation of the Store](#chapter-1-the-curse-of-fhs-and-the-salvation-of-the-store)
  - [Chapter 2: Daily Life with the Guix CLI](#chapter-2-daily-life-with-the-guix-cli)
  - [Chapter 3: Channels, Pins, and Time Travel](#chapter-3-channels-pins-and-time-travel)
- [**Part II: The Development Wonderland — Escaping Dependency Hell**](#part-ii-the-development-wonderland--escaping-dependency-hell)
  - [Chapter 4: Goodbye Virtualenvs, Hello `guix shell`](#chapter-4-goodbye-virtualenvs-hello-guix-shell)
  - [Chapter 5: Project Manifests and Package Transformations](#chapter-5-project-manifests-and-package-transformations)
- [**Part III: The Operating System — Declarative Computing & Shepherd**](#part-iii-the-operating-system--declarative-computing--shepherd)
  - [Chapter 6: Guix System: One File to Rule Them All](#chapter-6-guix-system-one-file-to-rule-them-all)
  - [Chapter 7: GNU Shepherd: The Lisp-Powered Init System](#chapter-7-gnu-shepherd-the-lisp-powered-init-system)
  - [Chapter 8: Guix Home: Declarative Dotfiles and Userland](#chapter-8-guix-home-declarative-dotfiles-and-userland)
- [**Part IV: The Master Craftsman — Packaging with Scheme**](#part-iv-the-master-craftsman--packaging-with-scheme)
  - [Chapter 9: The Anatomy of a Package](#chapter-9-the-anatomy-of-a-package)
  - [Chapter 10: Build Phases, G-Expressions, and Shebangs](#chapter-10-build-phases-g-expressions-and-shebangs)
  - [Chapter 11: Rolling Your Own Custom Channel](#chapter-11-rolling-your-own-custom-channel)
- [**Part V: The Real-World Frontier — Deployment, Domains & Pragmatic Hardware**](#part-v-the-real-world-frontier--deployment-domains--pragmatic-hardware)
  - [Chapter 12: Standalone Bundles: `guix pack` for Docker, AppImage, and HPC](#chapter-12-standalone-bundles-guix-pack-for-docker-appimage-and-hpc)
  - [Chapter 13: Guix in the Wild: Domain Impact and Taming Real Hardware with Nonguix](#chapter-13-guix-in-the-wild-domain-impact-and-taming-real-hardware-with-nonguix)
  - [Chapter 14: The Alchemist's Workbench: Practical Debugging, REPL Mastery, and Emacs Workflows](#chapter-14-the-alchemists-workbench-practical-debugging-repl-mastery-and-emacs-workflows)
  - [Chapter 15: The Twin Souls: GNU Emacs and the Living Lisp Machine](#chapter-15-the-twin-souls-gnu-emacs-and-the-living-lisp-machine)
- [**Appendices**](#appendices)
  - [Appendix A: The Ultimate Guix Cheat Sheet](#appendix-a-the-ultimate-guix-cheat-sheet)
  - [Appendix B: Troubleshooting and Common Footguns](#appendix-b-troubleshooting-and-common-footguns)
- [**Building Offline Editions (PDF & EPUB)**](#building-offline-editions)
- [**License & Acknowledgments**](#license)

---

<a id="dedication"></a>

## Dedication

> *Dedicated to everyone who ever ran `sudo apt-get dist-upgrade` at 4:58 PM on a Friday and spent the entire weekend staring at a broken X server and crying into an unbootable kernel.*
>
> *To all the developers whose software "works on my machine" and immediately bursts into flames on anyone else's.*
>
> *And to the humble parenthesis `()`, without which this entire universe would dissolve into an unstructured chaos of arbitrary YAML indents.*

<br/>

**Colophon**  
This book was typeset with LaTeX using `pdflatex`. The code examples were validated against GNU Guix on GNU/Linux. No global states, mutable `/usr/lib` symlinks, or Python virtualenvs were harmed in the making of this manuscript. All builds are bit-for-bit reproducible, give or take cosmic rays.

[⬆ Back to Table of Contents](#-table-of-contents)



## Preface: The Imperative Hellscape and the Functional Cure

> *""Computers are fast because they do exactly what you tell them to do. Computers are broken because what you told them to do was insane.""*
> 
> — **Anonymous Systems Engineer**

Let us begin with a moment of silence for the countless hard drives, continuous integration servers, and weekend plans destroyed by the following phrase:

**`sudo apt-get upgrade -y`**

You know the feeling. You run the command innocently because you wanted a slightly newer version of a text editor. Suddenly, 412 packages are being downloaded. `libc6` is being replaced in-place while your running processes are actively executing its memory pages. A post-install script written by an overcaffeinated maintainer in 2008 runs an interactive dialog box in the background, locks the DPKG database, and when your machine reboots, your graphical interface has been replaced by a blinking cursor and an existential dread.

Welcome to the **Imperative Hellscape**.

<div align="center">
  <img src="images/preface_hellscape_zen.jpg" width="720" alt="Figure 0.1: The choice is yours: constant panic in the imperative flames, or peaceful functional enlightenment with GNU Guix."/>
  <br/>
  <em>Figure 0.1: The choice is yours: constant panic in the imperative flames, or peaceful functional enlightenment with GNU Guix.</em>
</div>

### The Root of All Sysadmin Evil: Mutable State

For fifty years, the Unix philosophy built miraculous tools on a foundation of sand: the **Filesystem Hierarchy Standard (FHS)**. In FHS, there is exactly one place where shared libraries go: `/usr/lib`. There is one place where binary executables go: `/usr/bin`.

Think of `/usr/bin` as a communal refrigerator in a student dorm shared by thirty messy roommates:

  - Alice puts her carton of milk (Python 3.9) in the fridge.
  - Bob comes along, decides he needs oat milk (Python 3.11), throws Alice's milk in the dumpster, and puts his oat milk in the exact same spot.
  - Carol tries to make coffee with Alice's milk, discovers an oat-flavored disaster, and the entire kitchen explodes with `ImportError: symbol not found`.

Every time you run `apt`, `dnf`, `pacman`, or `brew`, you are mutating a single global state. When two programs need different versions of the same shared library, traditional systems resort to terrifying hacks:

  - **Virtual environments** (e.g., Python `venv`, Node `node_modules`): Dumping 80,000 duplicated tiny files in every single directory on your hard drive until your SSD groans in agony.
  - **Docker containers**: Shipping an entire 2-gigabyte Debian operating system just to run a 10-line Python script because you gave up on resolving dependencies cleanly.
  - **Flatpak / Snap**: Bundling runtime runtimes inside bundles inside sandbox layers.

> [!CAUTION]
> **😭 Tears of the Imperative Developer: The Packaging Band-Aid Pyramid**
>
> First, we had `tar.gz`. Then we had `dpkg` and `rpm` to track what was overwritten. When dependencies tangled into knots, we created `apt` and `yum` to untangle the knots. When global dependencies broke, we invented Python virtualenvs, Ruby rbenv, and Node nvm. When those still leaked system libraries, we shoved everything into 1.5GB Docker images. When Docker images drifted over time, we invented Kubernetes to orchestrate the chaos.
>
> At no point did anyone pause and ask: *"What if we stopped overwriting files in `/usr/lib` like cavemen?"*

### The Functional Epiphany

In 2006, a Dutch computer scientist named Eelco Dolstra published a doctoral dissertation introducing **purely functional package management**. The core thesis is mind-bendingly simple:

$\text{Package} = f(\text{Source Code}, \text{Compiler}, \text{Dependencies}, \text{Build Flags})$

In pure mathematics, $2 + 2$ is always $4$. If you call $f(x)$, you get the same result every time, without setting fire to the chalkboard. Why should compiling software be any different?

If a package is a pure mathematical function of its inputs, then:

  - Every package build can live in an immutable, read-only directory named after the cryptographic hash of all its inputs:
  
  `/gnu/store/8h3j2n9k4...-python-3.10.7`
  
  - Multiple versions of Python, OpenSSL, or GCC can coexist simultaneously without knowing or caring about each other.
  - Upgrading a package is simply moving a symlink. If you don't like the upgrade, moving the symlink back is an instantaneous, zero-risk **rollback**.

### Why GNU Guix? (And Why Scheme?)

While Nix pioneered functional package management, it invented its own idiosyncratic, domain-specific configuration language.

**GNU Guix** took this functional paradigm and made a radical, glorious choice: **Everything is GNU Guile Scheme.**

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: The Power of Scheme**
>
> In Guix, your package definitions are Scheme. Your system configuration is Scheme. Your init system (GNU Shepherd) is Scheme. Your build phases are Scheme. Your dotfiles are Scheme.
>
> There is no boundary between "configuration data" and "real code". You have the full power of a battle-tested, general-purpose, Lisp-dialect programming language with macros, first-class functions, and interactive REPL debugging at every layer of the operating system stack.

Yes, there will be parentheses. Many parentheses. But do not be afraid! As you read through this book, you will discover that those parentheses are not visual noise; they are the armor that protects your operating system from corruption.

### How This Book Is Structured

  - **Part I: The Grand Illusion (Package Management)**: We explore the immutable store (`/gnu/store`), unprivileged package management on foreign Linux distributions, transactional profiles and rollbacks, channels, and time travel with `guix time-machine`.
  - **Part II: The Development Wonderland**: We ditch Docker and virtualenvs for `guix shell`, explore isolated containers, write `manifest.scm` files, and integrate with `direnv`.
  - **Part III: The Operating System (Guix System & Guix Home)**: We build declarative, fully reproducible operating systems using a single `config.scm`, explore the Scheme-powered Shepherd init system, and manage our personal dotfiles with `guix home`.
  - **Part IV: The Master Craftsman (Packaging with Guix)**: We learn how to write our own package recipes, master build systems, tame build phases, write G-Expressions (`#\~{}`), and publish our own custom channels.
  - **Part V: The Real-World Frontier (Deployment, Domains & The Living Lisp Machine)**: We escape the Guix bubble with `guix pack` to generate standalone relocatable bundles for HPC clusters, Docker/OCI images without Docker, AppImages for desktop users, and direct store transfers via `guix copy` and `guix archive`. Then, we examine Guix's real-world impact across science and industry, and show how Nonguix tames modern laptops, Wi-Fi chips, and NVIDIA GPUs. Next, we master practical debugging workflows, REPL-driven system introspection, and source navigation. Finally, we explore the sacred alliance between GNU Guix and GNU Emacs—resurrecting the unified, living Lisp Machine from bootloader to editor buffers.
  - **Appendices**: The ultimate cheat sheet and troubleshooting guide for escaping any bind.

Buckle your seatbelt, fire up your terminal, and let us venture into the serene, reproducible promised land of GNU Guix.

[⬆ Back to Table of Contents](#-table-of-contents)



---

# Part I: The Grand Illusion — Package Management Done Right



## Chapter 1: The Curse of FHS and the Salvation of the Store

> *""Inside every large operating system is an FHS structure struggling to corrupt itself.""*
> 
> — **The Tao of Declarative Systems**

To understand why GNU Guix exists, we must first confront the original sin of modern Unix systems: the **Filesystem Hierarchy Standard (FHS)**. 

If you open up an ordinary Linux system (Ubuntu, Fedora, Arch, or Debian), you will see directories named `/bin`, `/sbin`, `/usr/bin`, `/lib`, and `/usr/lib`. These directories are what computer scientists technically refer to as *"a giant mutable pile of shared state that everyone writes to and hopes nobody touches."*

### The Myth of the Shared Library

In the 1970s and 1980s, computer storage was measured in kilobytes. A hard drive holding 10 megabytes was the size of a washing machine and cost more than a family sedan. In that era, sharing dynamic libraries (`.so` files) in a global directory like `/usr/lib` was an absolute necessity.

Today, your smartphone has 256 gigabytes of solid-state storage, but your server still crashes because Package A upgraded `libssl.so.1.1` to `libssl.so.3.0`, instantly breaking Package B, which was compiled against the older ABI.

> [!CAUTION]
> **😭 Tears of the Imperative Developer: The Dependency Diamond of Doom**
>
> Consider three software packages:
> 
>   - Your critical application needs **Library X** (version 1.0) and **Library Y** (version 2.0).
>   - **Library X** requires **LibZ** (version 1.4).
>   - **Library Y** requires **LibZ** (version 2.1).
> 
> In an FHS system, `/usr/lib/libz.so` can only point to one file. You are now trapped in dependency hell. Your package manager will either refuse to install the software, or it will overwrite `libz.so` and silently turn your application into a source of random segmentation faults.

### The Holy Store: /gnu/store

GNU Guix throws the FHS model straight out the window. In Guix, there is no global `/usr/bin` or `/usr/lib`. Instead, every piece of software, every library, every configuration file, and every script lives in an isolated, read-only sanctuary called the **Store**:

`/gnu/store/`

Every directory inside `/gnu/store` has a very specific, deterministic naming convention:

`/gnu/store/`**7yv4938r4wbz9p42x...**-**coreutils-9.1**

What is that 32-character gibberish at the front? That is a **base32 cryptographic hash** of all the inputs used to build that exact package.

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: What Goes into the Hash?**
>
> The cryptographic hash prefix is NOT simply the hash of the source code archive! It is computed from the complete graph of dependencies:
> 
>   - The source code tarball / git commit and its checksum.
>   - The build scripts, flags, and patches.
>   - The exact compiler binary (e.g., GCC 11.3.0) and its own dependency hash.
>   - The exact C library (`glibc`) used during linking.
>   - All transitive libraries and build-time tools.
> 
> If even a single compiler flag or dependency changes by one bit, the hash changes completely, resulting in a completely distinct directory in `/gnu/store`.

Because of this, you can have 14 different versions of Python, 5 versions of GCC, and 3 different builds of OpenSSL coexisting peacefully in `/gnu/store`. They never collide. They never overwrite each other.

<div align="center">
  <img src="images/store_vs_fridge.jpg" width="720" alt="Figure 1.1: A Tale of Two Stores: The chaotic communal dorm fridge of `/usr/bin` versus the immutable crystal vault of `/gnu/store`."/>
  <br/>
  <em>Figure 1.1: A Tale of Two Stores: The chaotic communal dorm fridge of `/usr/bin` versus the immutable crystal vault of `/gnu/store`.</em>
</div>

### Derivations: The Recipe Behind the Magic

Before Guix builds anything, it generates a low-level recipe called a **Derivation** (stored as a `.drv` file in `/gnu/store`). 

A derivation is a completely serializable, language-agnostic description of an action to perform. You can think of it as an immutable build plan that specifies:

  - The inputs required (other store paths).
  - The build environment (environment variables, architecture).
  - The builder executable to invoke (often Guile or a shell script).
  - The expected output paths in `/gnu/store`.

When you ask Guix to install or build a package, Guile evaluates your high-level Scheme code, translates it into a derivation graph (a Directed Acyclic Graph, or DAG), and hands it over to the background build daemon (`guix-daemon`).

### The Isolated Build Sandbox

How does Guix guarantee that a build doesn't secretly depend on some random file sitting in `/tmp` or a global header file?

When the `guix-daemon` executes a derivation, it puts the build process inside an ultra-strict, isolated **chroot sandbox**:

  - **No Network Access**: The builder has no internet connectivity during the build phase (unless it is a dedicated fixed-output download derivation with a verified cryptographic hash).
  - **Clean Environment**: All host environment variables are stripped away. Only variables explicitly declared in the derivation exist.
  - **Hermetic Filesystem**: The only files visible to the build process are the explicitly declared input store paths and an empty temporary build directory.
  - **Time Travel to 1970**: The file timestamps inside the build directory are normalized to January 1, 1970, 00:00:01 UTC. This prevents build tools (like `zip` or `tar`) from baking non-deterministic timestamps into their binaries!

> [!WARNING]
> **⚠️ Caution: Footgun Detected!: The Impure Build Assumption**
>
> If you are used to building software on Ubuntu where your `Makefile` secretly relies on `/usr/include/some-header.h` that you installed five years ago and forgot about, Guix will immediately slap your hand and fail the build. In Guix, if an input is not explicitly declared in Scheme, it does not exist in the universe.

### Profiles and Generations: The Symlink Forest

If everything is buried inside an unreadable hash path like:

`/gnu/store/7yv4938r4wbz9p42x...-coreutils-9.1/bin/ls`

how on earth does a normal user run `ls` from their command line?

Guix solves this through **Profiles** and **Generations**.

  - A **Profile** is simply a directory containing symlinks pointing into various store paths. It mimics a standard Unix hierarchy (`bin/`, `lib/`, `share/`).
  - Your shell's `$PATH` simply points to `~/.guix-profile/bin`.
  - Whenever you install or remove software, Guix builds a new store item representing the merged union of all your installed packages. This new union becomes **Generation $N+1$**.
  - Guix updates the symlink `~/.guix-profile` to point to Generation $N+1$ using an **atomic rename** system call.

| **Symlink Pointer** |  | **Target Destination** |
| :--- | :--- | :--- |
| `~/.guix-profile` | → | `/var/guix/profiles/per-user/alice/guix-profile` |
| `guix-profile` | → | `guix-profile-42-link` |
| `guix-profile-42-link` | → | `/gnu/store/...-profile/bin/ls` |
| `guix-profile-41-link` | → | `/gnu/store/...-profile/bin/ls` (Rollback target) |

Because switching generations is literally just changing a single symbolic link, **installing packages is instantaneous and atomic**. If your laptop battery dies in the middle of a 4-gigabyte installation, your running profile is completely untouched. You cannot get a corrupted, half-installed system.

And if you hate the new version? You simply flip the symlink back to the previous generation.

### Two Operating Modes: Foreign Distros and Guix System

Before we jump into the command line, one foundational distinction must be highlighted. GNU Guix can be operated in two fundamentally different modes:

  - **As a Package Manager on a "Foreign" Distribution**: You install Guix on top of an existing, traditional Linux distribution such as Debian, Ubuntu, Fedora, openSUSE, or Arch Linux. In this setup, Guix coexists harmoniously alongside your host system's native package manager (`apt`, `dnf`, `pacman`). The host OS continues to handle your kernel, hardware drivers, and system daemons, while Guix provides an unprivileged, isolated `/gnu/store` and per-user profiles. You get reproducible packages, atomic rollbacks, and multi-version library coexistence without altering the underlying OS.
  - **As a Complete Operating System (Guix System)**: Guix can also replace your entire traditional distribution. In Guix System, everything—from the Linux kernel, bootloader, Shepherd init system, and background daemons to user accounts and desktop environments—is declared within a unified Scheme configuration file (`/etc/config.scm`).

Throughout Part~I and Part~II of this book, we will primarily explore Guix through the lens of a package manager running on a foreign distribution. As you will see in [Chapter 2](#chapter-2-daily-life-with-the-guix-cli), the familiar, non-declarative commands for installing software (`guix install`) are uniquely suited to foreign distributions—whereas on Guix System, declarative configuration takes center stage.

[⬆ Back to Table of Contents](#-table-of-contents)



## Chapter 2: Daily Life with the Guix CLI

> *""There are two types of sysadmins: those who have broken production with an update, and those who are about to.""*
> 
> — **Murphy's Law of Operations**

Now that you understand that `/gnu/store` is a cryptographic citadel of immutable purity, let us roll up our sleeves and interact with the Guix command-line interface.

Unlike traditional package managers that demand `sudo` permissions to modify the global system state, Guix package management is entirely **unprivileged**. Every user on the system can install, upgrade, and remove software in their own user profile without ever asking the sysadmin for permission.

### The Non-Declarative CLI: A Foreign Distro Lifeline

Before typing our first installation command, we must address an essential philosophical question: *How does the Guix command-line interface fit into the functional, declarative vision of GNU Guix?*

The commands introduced in this chapter—`guix install`, `guix remove`, and `guix upgrade`—represent the **imperative**, or **non-declarative**, style of package management. In an imperative model, you type sequential commands to mutate your active user profile step by step over time.

It is crucial to understand that **this non-declarative way of installing packages mainly applies when Guix is used as an auxiliary package manager on a distribution other than Guix System** (what the Guix community terms a **foreign distribution**, such as Debian, Ubuntu, Fedora, openSUSE, or Arch Linux).

#### Why the Non-Declarative Model Thrives on Foreign Distros

When you install GNU Guix on top of Ubuntu or Debian, you do not control the base operating system with Guix; your host kernel, systemd init system, display manager, and base utilities are all governed by the host distribution. In this environment, your goals are practical and immediate:

  - You want cutting-edge software or specific development tools without waiting for your host distribution's slow release cycle.
  - You lack `sudo` or root privileges on a shared university cluster or corporate workstation.
  - You need to run conflicting libraries side-by-side without contaminating the host system's `/usr/lib`.

In this foreign distribution setting, running `guix install` is wonderfully liberating. It acts as a direct, unprivileged replacement for traditional package managers like `apt` or `brew`, yet bestows the mathematical superpowers of the Store: atomic transactions, zero dependency conflicts, and instantaneous rollbacks.

#### Why Guix System Purists Avoid `guix install`

Conversely, if you are running **Guix System**—where Guix is the standalone operating system—this non-declarative approach is largely considered an **anti-pattern** and is discouraged for permanent workstation setups.

Why? Because Guix System is built on the core tenet that **the file is the machine**:

  - System packages belong in the `packages` field of your declarative `/etc/config.scm` ([Chapter 6](#chapter-6-guix-system-one-file-to-rule-them-all)).
  - User tools and dotfiles belong in a declarative home environment managed by **Guix Home** ([Chapter 8](#chapter-8-guix-home-declarative-dotfiles-and-userland)) or project-specific manifests ([Chapter 5](#chapter-5-project-manifests-and-package-transformations)).
  - Temporary, disposable tools are best invoked on-demand using ephemeral `guix shell` environments ([Chapter 4](#chapter-4-goodbye-virtualenvs-hello-guix-shell)).

If you run `guix install` on Guix System, you create an unversioned, mutable profile under `~/.guix-profile`. If your hard drive fails or you replicate your environment on another computer, those imperatively installed packages will be completely absent because they were never committed to your declarative Scheme configuration!

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: Non-Declarative CLI vs. Declarative Configuration**
>
> 
>   - **Non-Declarative (`guix install`, `guix remove`)**:
>   Best suited for foreign distros (Debian, Ubuntu, Fedora) and fast ad-hoc experimentation. State is tracked via profile generations in `/var/guix/profiles`, but cannot be fully reproduced on another machine without replaying your shell history.
>   - **Declarative (`config.scm`, Guix Home, Manifests)**:
>   The standard way on Guix System. State is declared in Scheme files tracked with Git. You reconfigure your system with `guix system reconfigure` or your user environment with `guix home reconfigure`. Any machine can be cloned with 100% mathematical precision.
> 

Why, then, do we begin our journey with the non-declarative CLI? Because it is the gentlest and most intuitive bridge from traditional package managers. It allows you to grasp profiles, generations, rollbacks, and garbage collection hands-on before we ascend to the declarative peaks of manifests and Guix System.

### Installing and Removing Packages

The most basic operations will look pleasantly familiar, with a subtle functional twist:
```bash
# Search for software (searches names, synopses, and descriptions)
guix search emacs

# Show detailed information about a package
guix show emacs-ripgrep

# Install a package into your active user profile
guix install htop git ripgrep

# Remove a package from your user profile
guix remove htop

# Upgrade all packages in your profile to their latest versions
guix upgrade
```

> [!WARNING]
> **⚠️ Caution: Footgun Detected!: The Imperative Trap on Guix System**
>
> If you are reading this while running Guix System, resist the urge to turn `guix install` into your daily routine! Imperatively installed packages live in an isolated profile outside your system's declarative `config.scm`. Treat the commands in this chapter as mastering the transactional mechanics of profiles and rollbacks, but save your permanent workstation setup for the declarative configurations in Part~II and Part~III.

> [!TIP]
> **💡 Guix Wizard Pro-Tip: Fast Searching with Recutils**
>
> When you run `guix search`, Guix evaluates the Scheme package records and outputs results formatted as `recutils` records. You can pipe the output into standard tools or filter fields:

> ```bash
> guix search emacs | grep -E '^name:'
> ```
>
> Or search strictly by package name without scanning full descriptions:

> ```bash
> guix search '^emacs$'
> ```
>

### The Miraculous Undo Button: Rollbacks

Suppose you ran `guix upgrade` on a Monday morning. The new version of your favorite software contains a catastrophic regression, or perhaps you accidentally uninstalled your text editor right before a deadline.

On an imperative distribution (Ubuntu, Arch, etc.), you would now be combing through cache archives, manually downloading `.deb` or `.pkg.tar.zst` files, and praying you don't trigger dynamic linker errors.

On Guix, you simply invoke the undo button:
```bash
# Instant rollback to the previous generation
guix package --roll-back
```

> [!CAUTION]
> **😭 Tears of the Imperative Developer: The 2-Millisecond Rescue**
>
> When you type `guix package –roll-back`, Guix does not download anything. It does not recompile anything. It merely updates the `~/.guix-profile` symlink to point back to Generation $N-1$. The entire rollback takes approximately 2 milliseconds. You can do it while running a live presentation and nobody in the audience will notice.

### Inspecting and Navigating Generations

Every transactional change to your profile creates a permanent historical record called a **Generation**. You can inspect the entire history of your user environment:
```bash
guix package --list-generations
```

This displays an informative timeline:
```bash
Generation 1    Oct 12 2025 14:02:11
 + git          2.41.0          out     /gnu/store/7a3...-git-2.41.0
 + ripgrep      13.0.0          out     /gnu/store/8bc...-ripgrep-13.0.0

Generation 2    Oct 14 2025 09:15:30
 + python       3.10.7          out     /gnu/store/9df...-python-3.10.7

Generation 3 (current)  Oct 15 2025 11:22:04
 - ripgrep      13.0.0          out     /gnu/store/8bc...-ripgrep-13.0.0
 + ripgrep      14.0.1          out     /gnu/store/2ea...-ripgrep-14.0.1
```

You can switch to any arbitrary point in your history at will:
```bash
# Travel directly to Generation 1
guix package --switch-generation=1
```

### Multiple Custom Profiles

Why cram your video editor, your Haskell compiler, your audio synthesizer, and your scientific Python stack into a single bloated user profile?

In Guix, you can instantiate as many independent profiles as you want by passing the `-p` or `–profile` flag:
```bash
# Create a dedicated profile for audio production
guix package -p ~/profiles/audio -i ardour jack2 audacity

# Create a dedicated profile for data science
guix package -p ~/profiles/datascience -i python python-numpy python-scipy

# Activate a custom profile in your current shell
source ~/profiles/audio/etc/profile
```

When you source `etc/profile`, Guix automatically configures your environment variables (`PATH`, `LIBRARY_PATH`, `GUIX_PYTHONPATH`, etc.) for that specific set of packages.

> [!TIP]
> **💡 Guix Wizard Pro-Tip: Declarative Profiles with Manifests**
>
> While we create custom profiles imperatively in this chapter using `-i`, Guix also lets you instantiate and update profiles **declaratively** from a Scheme manifest file:

> ```bash
> guix package -p ~/profiles/datascience -m manifest.scm
> ```
>
> This combines the isolation of separate profiles with the reproducibility of source-controlled configuration, which we explore in [Chapter 5](#chapter-5-project-manifests-and-package-transformations).

### Garbage Collection and Disk Space Management

Because Guix keeps old generations around to make rollbacks instantaneous, your `/gnu/store` will eventually grow larger as you install and upgrade software over months.

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: How Garbage Collection Works**
>
> Guix uses a tracing garbage collector, similar to programming language runtimes (like Java, Go, or Guile).
> 
>   - **GC Roots**: Guix scans known roots (active user profiles, system generations, running processes, and pins in `/var/guix/gcroots`).
>   - **Liveness Trace**: Any store item that can be reached via symlinks or references from an active root is marked as **live**.
>   - **Reclamation**: Any store item that is completely unreferenced is deleted from disk.
> 

If you simply run `guix gc`, it will only remove packages that are not referenced by **any** generation of any profile. To reclaim significant space, you first delete historical generations you no longer need:
```bash
# Delete all profile generations older than 30 days
guix package --delete-generations=30d

# Delete all generations except the current one
guix package --delete-generations

# Run the garbage collector to reclaim unused disk space
guix gc

# Free disk space down to a target size (e.g., free at least 10GB)
guix gc -F 10G
```

> [!WARNING]
> **⚠️ Caution: Footgun Detected!: The Premature GC Trap**
>
> If you delete your old generations with `guix package –delete-generations` and then immediately run `guix gc`, your previous generations are gone forever. You will no longer be able to roll back to yesterday's profile! Keep at least a few days of generations around unless you are in desperate need of disk space.

### Substitutes: Why You Do Not Have to Compile Everything

A common fear among newcomers is: *"If Guix is functional and source-based, am I going to spend the next four days compiling Firefox and Chromium from source?"*

The answer is **no**. Guix uses **Substitutes** (pre-built binary caches signed by trusted continuous integration servers like `ci.guix.gnu.org` and `bordeaux.guix.gnu.org`).

When Guix determines that a derivation hash `/gnu/store/abc123...-firefox-115.0.drv` is needed, it checks if a trusted substitute server already built that exact derivation. If it exists, Guix simply downloads the pre-built cryptographic narball (normalized archive) and unpacks it into your store. You get all the speed of a binary package manager with all the mathematical purity of a source-based functional system.

### The Road Ahead: Beyond Non-Declarative Mutations

The non-declarative CLI commands covered in this chapter provide an immediate, dependable upgrade for anyone running Guix on a foreign distribution. You can install, upgrade, and rollback software without root privileges and without fear of library collision.

Yet, imperative management has a fundamental ceiling: your environment remains an artifact of whatever sequence of commands you typed into your terminal over the past six months. In the upcoming chapters, we will transcend imperative mutations:

  - In [Chapter 3](#chapter-3-channels-pins-and-time-travel), we pin the package tree to precise Git revisions and travel through time.
  - In [Chapter 4](#chapter-4-goodbye-virtualenvs-hello-guix-shell) and [Chapter 5](#chapter-5-project-manifests-and-package-transformations), we replace permanent profile installations with ephemeral shells and version-controlled manifests.
  - In [Chapter 6](#chapter-6-guix-system-one-file-to-rule-them-all) and [Chapter 8](#chapter-8-guix-home-declarative-dotfiles-and-userland), we achieve full declarative mastery over entire operating systems and user homes.

[⬆ Back to Table of Contents](#-table-of-contents)



## Chapter 3: Channels, Pins, and Time Travel

> *""Those who cannot remember their dependencies are condemned to repeat their compilation errors.""*
> 
> — **George Santayana (adapted for sysadmins)**

By default, GNU Guix provides thousands of packages in its official repository. But what if you need packages that are not in the main tree, proprietary drivers for your laptop's Wi-Fi card, cutting-edge bioinformatics pipelines, or your company's proprietary microservices?

Welcome to the world of **Channels**.

### What Is a Channel?

In Guix, a **Channel** is not an opaque binary PPA or an unverified APT repository. 

A channel is simply a **Git repository** containing Scheme source files that define packages and services. When you run `guix pull`, Guix clones each channel repository, verifies its cryptographic commit signatures, compiles the Scheme modules, and builds a brand-new `guix` executable and package database.

### Configuring Channels: `~/.config/guix/channels.scm`

You configure your active channels by creating a Scheme file at `~/.config/guix/channels.scm`.

Let us examine a typical multi-channel configuration:
```scheme
;; ~/.config/guix/channels.scm
(list
  ;; 1. The official GNU Guix channel (always required)
  (channel
    (name 'guix)
    (url "https://git.savannah.gnu.org/git/guix.git")
    (branch "master")
    ;; Cryptographic introduction for commit authentication
    (introduction
      (make-channel-introduction
        "9edb3f66fd807b096b48283debd4ddcc33ab9a99"
        (openpgp-fingerprint
          "BBB0 2DDF 2CEA F6A8 0D1D  E643 A2A0 6DF2 A33A 54FA"))))

  ;; 2. Nonguix: Non-free drivers, firmware, and proprietary software
  (channel
    (name 'nonguix)
    (url "https://gitlab.com/nonguix/nonguix")
    (branch "master")
    (introduction
      (make-channel-introduction
        "2a97b46e96194b703221a074ddb4402d5dd99708"
        (openpgp-fingerprint
          "2A39 3FFF 68F4 EF7A 3D29  12AF 6F51 20A0 22FB B2D5"))))

  ;; 3. Guix Science: Scientific software and HPC packages
  (channel
    (name 'guix-science)
    (url "https://codeberg.org/guix-science/guix-science.git")
    (branch "master")
    (introduction
      (make-channel-introduction
        "b3a5e796aa404a60773b06cf317b3e51240366eb"
        (openpgp-fingerprint
          "CA4D 7EB7 5D15 73A8 E426  3850 5F12 30A0 CFFB 97BE")))))
```

### Notable Custom Channels

The Guix ecosystem features several essential community channels that expand your package universe:

  - **Nonguix**: Provides packages that cannot be included in upstream GNU Guix due to the GNU Free System Distribution Guidelines (FSDG). This includes the vanilla Linux kernel (`linux`), proprietary Wi-Fi firmware (`linux-firmware`), Steam, Spotify, Google Chrome, and NVIDIA drivers.
  - **Guix Science**: High-Performance Computing (HPC), bioinformatics, computational biology, machine learning (PyTorch, JAX), and computer vision pipelines maintained by academic research institutes worldwide.
  - **Guix Past**: A historical channel containing legacy toolchains, GCC 2.95, Python 2.4, and ancient libraries needed to reproduce scientific papers published 15 years ago.

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: Channel Authentication with OpenPGP**
>
> Notice the `introduction` block in each channel definition! Guix uses cryptographic OpenPGP signatures on every single Git commit in a channel. 
> If an attacker compromises GitHub or GitLab and pushes a malicious commit without a valid signature from an authorized developer key, `guix pull` will abort with a security failure before executing any code.

### Authorizing Pre-Built Substitutes for Channels

When using external channels like Nonguix or Guix Science, you don't have to compile large software packages (like the Linux kernel or PyTorch) locally from scratch. Each channel maintains dedicated build farms that serve pre-built binaries (substitutes).

To authorize these substitute servers, add their signing keys and URLs to your system configuration:
```bash
# Download and authorize the Nonguix signing key
wget https://substitutes.nonguix.org/signing-key.pub
sudo guix archive --authorize < signing-key.pub

# Update your Guix daemon with the substitute URL
sudo herd set-substitute-urls guix-daemon \
  https://substitutes.nonguix.org \
  https://bordeaux.guix.gnu.org \
  https://ci.guix.gnu.org
```

### Channel Pins: Locking Reality

How do you guarantee that a colleague running `guix pull` gets the exact same package versions you have today?

You **pin** your channels to specific Git commit hashes:
```scheme
;; Pinned channels.scm for guaranteed reproducibility
(list
  (channel
    (name 'guix)
    (url "https://git.savannah.gnu.org/git/guix.git")
    (commit "a84ef2b9d3e817921a415a77c3e53381a1795c64"))
  (channel
    (name 'nonguix)
    (url "https://gitlab.com/nonguix/nonguix")
    (commit "92e104c8f01bcf5594b2efc8f74f1b8a5b23d9b0")))
```

You can generate this pinned configuration automatically from your current system state with:
```bash
guix describe -f channels > channels.scm
```

This produces an exact, machine-readable Scheme file representing the precise Git commit hashes of all active channels (`guix`, `nonguix`, `guix-science`).

If you commit that output to a file named `channels.scm`, anyone can reproduce your multi-channel universe down to the exact bit using `guix time-machine`.

### The Superpower: `guix time-machine`

Now comes the coup de gr\^ace that makes every other package manager look like an antique.

Suppose you have a `channels.scm` file containing pins for GNU Guix and Guix Science from three years ago. You want to re-run an experiment today:
```bash
# Run an ad-hoc shell using the exact multi-channel universe from channels.scm
guix time-machine -C channels.scm -- shell python-pytorch r-ggplot2 -- python3 pipeline.py

# Or travel to a specific historic commit on the fly!
guix time-machine --commit=a84ef2b9d3... -- install emacs
```

<div align="center">
  <img src="images/time_machine.jpg" width="720" alt="Figure 3.1: Traveling through the cosmic timeline: `guix time-machine` seamlessly executing 10-year-old scientific code with zero dependency drift."/>
  <br/>
  <em>Figure 3.1: Traveling through the cosmic timeline: `guix time-machine` seamlessly executing 10-year-old scientific code with zero dependency drift.</em>
</div>

> [!CAUTION]
> **😭 Tears of the Imperative Developer: Scientific Reproducibility: A Solved Problem**
>
> In 2016, a survey in *Nature* revealed that over 70% of researchers had failed to reproduce another scientist's computational experiments due to dependency drift.
>
> With `guix time-machine` and multi-channel pins, scientific pipelines can be re-executed 10 years later producing identical numerical results.

[⬆ Back to Table of Contents](#-table-of-contents)



---

# Part II: The Development Wonderland — Escaping Dependency Hell



## Chapter 4: Goodbye Virtualenvs, Hello `guix shell`

> *""Docker: Because why solve dependency hell cleanly when you can just ship an entire Debian virtual machine for a 50-line Node.js script?""*
> 
> — **Modern DevOps proverb**

Every software developer has experienced the nightmare of setting up a new development project:

  - You clone the repository.
  - The `README.md` tells you to install GCC 12, CMake 3.25, Python 3.10, PostgreSQL 14 client headers, and a very specific version of Rust.
  - Your host operating system has GCC 14, Python 3.12, and CMake 3.20.
  - You spend the next five hours fighting PPA repositories, Homebrew taps, and Docker permission issues.

GNU Guix introduces the ultimate developer superpower: `guix shell`.

### The Concept: Disposable, Ephemeral Environments

`guix shell` allows you to spawn a subshell containing any set of packages on demand, without polluting your user profile, without root permissions, and without touching your system's global files.

When you exit the subshell, the environment evaporates into thin air.
```bash
# Spawn a shell with Python, Numpy, and GCC ready to go
guix shell python python-numpy gcc-toolchain

# Inside the shell, everything is configured:
[env]$ python3 -c "import numpy as np; print(np.__version__)"
1.23.2
[env]$ gcc --version
gcc (GCC) 11.3.0

# Exit the shell, and your host environment is completely untouched
[env]$ exit
$ which python3
/usr/bin/which: no python3 in ($PATH)
```

You can also run one-off commands directly without even dropping into an interactive prompt:
```bash
# Run a one-liner inside a disposable Node.js environment
guix shell node -- node -e "console.log('Hello from Guix!')"
```

### Achieving True Isolation: `–pure`

By default, `guix shell` merges the specified packages with your host environment variables (like your existing `$PATH`). This is convenient for daily use, but what if you want to be 100% sure your code doesn't accidentally depend on some random binary hidden in `/usr/local/bin`?

You add the `–pure` flag:
```bash
guix shell --pure python python-requests -- python3 app.py
```

When `–pure` is specified, Guix clears almost all host environment variables. Only the packages explicitly declared on the command line exist in `$PATH`.

### Containers Without Docker: The `-C` Flag

Now for the real magic. Guix contains a built-in container engine based on unprivileged Linux kernel namespaces (mount, PID, network, IPC, and UTS namespaces).

By passing the `-C` (or `–container`) flag, Guix creates a lightweight, isolated Linux container on the fly:
```bash
guix shell --container python bash coreutils
```

Inside this container:

  - The filesystem contains **only** `/gnu/store` and an empty `/tmp`.
  - Your real `/home` directory is completely invisible.
  - The process cannot see or kill any processes running on the host system.
  - Network access is disabled by default!
  - You did **NOT** need `sudo`, a root daemon, or a Docker service running in the background.

> [!CAUTION]
> **😭 Tears of the Imperative Developer: Docker Daemon vs Guix Container**
>
> Docker requires a root-privileged daemon listening on a Unix socket, custom overlay filesystems, non-reproducible `Dockerfile` scripts that run `curl ... | bash`, and layers upon layers of cached bloat.
>
> `guix shell -C` uses native Linux kernel namespaces directly, boots in 50 milliseconds, shares the immutable `/gnu/store` directly with zero copy-on-write overhead, and is completely unprivileged.

<div align="center">
  <img src="images/docker_vs_guix_shell.jpg" width="720" alt="Figure 4.1: Containerization contrast: 50 tons of root-privileged Docker overhead crushing a 3-line script versus the weightless, unprivileged bubble of `guix shell –container`."/>
  <br/>
  <em>Figure 4.1: Containerization contrast: 50 tons of root-privileged Docker overhead crushing a 3-line script versus the weightless, unprivileged bubble of `guix shell –container`.</em>
</div>

### Fine-Grained Sharing: Filesystems and Network

What if your containerized application needs access to a local dataset or needs to make HTTP requests? Guix provides granular flags:
```bash
guix shell --container \
  --network \
  --expose=/data/images=/mnt/images:ro \
  --share=/home/user/workspace=/app \
  python python-torch \
  -- python3 /app/train.py
```

Let us break down these flags:

  - `–network` (or `-N`): Grants network namespace access (enables outbound/inbound internet).
  - `–expose=HOST=GUEST:ro`: Mounts a host directory inside the container as **read-only**.
  - `–share=HOST=GUEST`: Mounts a host directory inside the container with **read-write** permissions.

### The Instant Development Environment: `-D`

Suppose you want to contribute to an existing open-source package packaged in Guix, such as `inkscape`, `curl`, or `qemu`. 

How do you get all of its 50+ build dependencies, header files, libraries, and compilers set up on your machine?
```bash
# Enter a shell with all build dependencies of Inkscape installed!
guix shell -D inkscape
```

The `-D` (or `–development`) flag inspects the Guix package recipe for `inkscape`, gathers all of its `inputs`, `native-inputs`, and `propagated-inputs`, and drops you into a shell where every single build dependency is available. You can immediately run `cmake` and `make` without installing a single package globally!

> [!TIP]
> **💡 Guix Wizard Pro-Tip: The Development Flag on Local Recipes**
>
> You can even use `-D -f guix.scm` to load the development environment defined in your own project's local package file! We will explore this in [Chapter 5](#chapter-5-project-manifests-and-package-transformations).

[⬆ Back to Table of Contents](#-table-of-contents)



## Chapter 5: Project Manifests and Package Transformations

> *""Tell me what your software depends on, and I will tell you who you are: a reproducible wizard or an imperative gambler.""*
> 
> — **The Guix Hacker's Catechism**

Typing `guix shell python python-numpy gcc-toolchain make git ...` every time you open a terminal quickly becomes tedious. Furthermore, passing command-line arguments does not capture custom package variants or programmatic dependencies.

To turn your project's development environment into a version-controlled, shareable artifact, GNU Guix provides **Manifests** and **Package Transformations**.

### Writing a `manifest.scm`

A manifest is a small Guile Scheme file that returns a list of packages to be included in an environment.

There are two primary ways to write a manifest:

#### 1. The Specification Approach: `specifications->manifest`

If you simply want a list of packages by name, `specifications->manifest` is the most concise:
```scheme
;; manifest.scm - Simple specification manifest
(specifications->manifest
  '("python"
    "python-numpy"
    "python-pandas"
    "python-matplotlib"
    "jupyter"
    "gcc-toolchain"
    "make"))
```

#### 2. The Programmatic Approach: `packages->manifest`

Because manifests are written in a full general-purpose programming language, you can construct package lists using Scheme logic, conditionals, and module imports:
```scheme
;; manifest.scm - Programmatic manifest
(use-modules (gnu packages python)
             (gnu packages python-science)
             (gnu packages python-xyz)
             (gnu packages gcc)
             (gnu packages base)
             (guix packages))

(packages->manifest
  (list python
        python-scipy
        python-pytorch
        gcc-toolchain
        gnu-make))
```

### Automatic Manifest Discovery

When you run `guix shell` in a directory containing a `manifest.scm` file without specifying package arguments, Guix automatically detects and loads the manifest:
```bash
$ ls
manifest.scm  src/  Makefile

$ guix shell
[env]$ # All packages from manifest.scm are automatically active!
```

If you want to run your automated tests in a hermetic container using this manifest, it is as simple as:
```bash
guix shell --container --manifest=manifest.scm -- make test
```

### Package Transformations: Rewriting the Dependency Graph

What happens when you need to test your application against a custom Git branch of an upstream dependency, or compile your library with Clang instead of GCC, or replace OpenSSL with a patched security release?

In traditional package managers, this requires editing upstream spec files, maintaining custom binary repositories, or manually rebuilding dozens of packages.

Guix solves this with **Package Transformations**—dynamic, on-the-fly graph rewrites:
```bash
# 1. Swap source code with a local tarball or directory
guix shell --with-source=python-numpy=./custom-numpy.tar.gz python-numpy

# 2. Pin a dependency to a bleeding-edge Git branch
guix shell --with-branch=libpng=feature-neon inkscape

# 3. Swap one dependency for another across the ENTIRE graph!
guix shell --with-input=openssl=openssl@1.1 node

# 4. Build a package with Clang instead of default GCC
guix shell --with-c-toolchain=ffmpeg=clang-toolchain ffmpeg

# 5. Enable full debug symbols for gdb debugging
guix shell --with-debug-info=glibc --with-debug-info=python python
```

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: How Graph Rewriting Works**
>
> When you pass `–with-input=A=B`, Guix performs a recursive transformation on the derivation graph:
> 
>   - It traverses all packages in the requested dependency DAG.
>   - Every node that lists `A` as an input has its dependency pointer updated to `B`.
>   - All downstream packages are automatically rebuilt with their newly derived cryptographic store hashes.
> 
> This happens deterministically without mutating any files on your host system.

### Manifest Transformations in Scheme

You can also embed package transformations directly inside your `manifest.scm` file so that your entire team inherits them automatically:
```scheme
;; manifest.scm with embedded transformation
(use-modules (guix transformations)
             (gnu packages python)
             (gnu packages python-science))

(define transform-numpy
  (options->transformation
    '((with-branch . "python-numpy=main"))))

(packages->manifest
  (list (transform-numpy python-numpy)
        python-scipy))
```

### Seamless IDE Integration with `direnv`

Manually typing `guix shell` every time you `cd` into a project directory is good, but automatic activation upon entering the directory is even better.

Using `direnv`, you can automatically activate your Guix development environment whenever you enter the project directory:
```bash
# In your project root, create a .envrc file:
cat << 'EOF' > .envrc
eval "$(guix shell --search-paths)"
EOF

# Allow direnv to execute in this directory:
direnv allow
```

Now, whenever you open VS Code, Emacs, Neovim, or `cd` into the folder in your terminal, all compiler tools, language servers (like `pyright`, `rust-analyzer`, or `clangd`), and libraries are immediately available in your environment!

[⬆ Back to Table of Contents](#-table-of-contents)



---

# Part III: The Operating System — Declarative Computing & Shepherd



## Chapter 6: Guix System: One File to Rule Them All

> *""A configuration management system like Ansible or Puppet is like a robot that walks around your kitchen moving spices. Guix System is a 3D printer that manufactures a pristine kitchen from scratch on every change.""*
> 
> — **Overheard at FOSDEM**

Up to this point, we have used Guix on top of a foreign distribution (like Debian, Fedora, or Arch). But Guix is not just a package manager; it is also a complete, standalone operating system: **Guix System**.

In Guix System, your entire machine—kernel, init system, system daemons, user accounts, filesystems, network configuration, and desktop environment—is declared inside a single Guile Scheme file, typically called `/etc/config.scm`.

### The Imperative OS Trap vs The Declarative OS

On an ordinary Linux system:

  - You edit `/etc/network/interfaces` or fiddle with NetworkManager.
  - You manually edit `/etc/fstab` and pray you didn't typo the UUID.
  - You run `useradd`, `usermod`, and `visudo`.
  - You install PostgreSQL, tweak `postgresql.conf`, and run `systemctl enable postgresql`.

Six months later, your server is a delicate, undocumented snowflake. Nobody knows which packages were installed manually, which configuration files were edited, or how to recreate the machine if the hardware dies.

In Guix System, **the file is the machine**. If a service or package is not declared in your Scheme configuration, it does not exist on your system.

#### The Imperative Temptation vs. Declarative Reproducibility

Having read about package management in [Chapter 2](#chapter-2-daily-life-with-the-guix-cli), your very first instinct after booting into Guix System might be to open a shell and type:

`guix install git emacs firefox htop`

**Do not do this!** This is the single most common pitfall for newcomers arriving from traditional distributions like Debian, Arch, or Fedora.

In [Chapter 2](#chapter-2-daily-life-with-the-guix-cli), we emphasized that the non-declarative, imperative workflow (`guix install`, `guix remove`) is primarily intended for users running Guix as a supplementary package manager on top of a **foreign distribution**. On Guix System, relying on `guix install` actively destroys one of the operating system's greatest superpowers: **complete, mathematical reproducibility**.

Consider what happens if you install software imperatively on Guix System:

  - Packages are placed in an isolated, untracked profile under `~/.guix-profile`.
  - Those packages remain completely invisible to your declarative operating system definition.
  - If your SSD fails tomorrow, or you wish to provision an identical backup laptop or cloud server from your Git repository, those imperatively installed packages will be completely absent because they were never recorded in your configuration code!

On Guix System, **the official, recommended, and reproducible way to install new packages is declaratively through `/etc/config.scm`**. Instead of mutating the machine state with ad-hoc terminal commands, you declare your desired software in Scheme code, commit it to version control, and instantiate it with `guix system reconfigure`.

### The Anatomy of `config.scm`

Let us examine a complete, fully functional `config.scm` for a desktop workstation:
```scheme
;; /etc/config.scm - Declarative Guix System configuration
(use-modules (gnu)
             (gnu system nss))
(use-service-modules desktop networking ssh sddm)
(use-package-modules certs fonts gnome linux package-management)

(operating-system
  (host-name "guix-battlestation")
  (timezone "Europe/Paris")
  (locale "en_US.utf8")

  ;; Bootloader Configuration (UEFI GRUB)
  (bootloader (bootloader-configuration
                (bootloader grub-efi-bootloader)
                (targets '("/boot/efi"))
                (keyboard-layout keyboard-layout)))

  ;; Storage & Filesystems
  (file-systems (cons* (file-system
                         (mount-point "/")
                         (device (file-system-label "my-root"))
                         (type "ext4"))
                       (file-system
                         (mount-point "/boot/efi")
                         (device (uuid "1234-ABCD" 'fat))
                         (type "vfat"))
                       %base-file-systems))

  ;; User Accounts
  (users (cons (user-account
                 (name "alice")
                 (group "users")
                 (supplementary-groups '("wheel" "netdev" "audio" "video" "kvm"))
                 (home-directory "/home/alice"))
               %base-user-accounts))

  ;; System-wide packages
  (packages (append (list nss-certs     ; HTTPS Certificates
                          font-dejavu   ; Core fonts
                          git
                          emacs)
                    %base-packages))

  ;; System Daemons and Desktop Services
  (services (append (list (service openssh-service-type
                            (openssh-configuration
                              (port-number 2222)
                              (permit-root-login #f)))
                          (service gnome-desktop-service-type))
                    %desktop-services)))
```

#### Installing New Packages: The Declarative Workflow

Examine lines 67–71 in the configuration above. This `packages` field is where system-wide software installation actually happens on Guix System:
```scheme
;; System-wide packages
  (packages (append (list nss-certs     ; HTTPS Certificates
                          font-dejavu   ; Core fonts
                          git
                          emacs)
                    %base-packages))
```

When you want to install a new package on your machine, you do not execute an imperative terminal command. Instead, you follow a clean four-step declarative workflow:

  - **Search**: Find the package name using `guix search <query>`.
  - **Import**: Ensure the module containing the package definition is imported at the top of your `config.scm` via `use-package-modules` (for example, `(use-package-modules admin)` for `htop`, or `(use-package-modules version-control)` for `git`).
  - **Declare**: Add the package variable name to the `(list ...)` inside the `packages` field.
  - **Reconfigure**: Apply your changes across the operating system:
```bash
sudo guix system reconfigure /etc/config.scm
```

Guix immediately downloads pre-built substitutes or builds the package, creates a brand-new operating system generation, and links the binaries into the system profile. If you later decide to uninstall the software, you simply delete its line from `config.scm` and reconfigure again.

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: Why Declarative Code Trumps Imperative Commands**
>
> By declaring packages directly inside `config.scm`, you guarantee that:
> 
>   - **The Machine Is Source Code**: Your entire software environment is captured in plain text. You can commit your configuration to Git, review software additions in pull requests, and audit changes over years.
>   - **Effortless Replication**: Setting up a second workstation or replacement laptop takes zero manual guesswork. Clone your configuration, run `guix system reconfigure`, and you get an identical system down to the last library.
>   - **Synchronized Rollbacks**: If an added package introduces a bug or breaks your workflow, rolling back to the previous system generation in GRUB reverts the packages, kernel, and system daemons simultaneously as one cohesive unit.
> 

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: Service Composition with `append` and `modify-services`**
>
> Notice how services are combined using standard Scheme list operations!
> `%desktop-services` is simply a Scheme list containing dozens of core services (udev, elogind, dbus, network-manager, polkit, etc.).
> You can add services with `append` or `cons`, or modify existing service configurations using the `modify-services` macro:

> ```scheme
> (modify-services %desktop-services
>   (guix-service-type config =>
>     (guix-configuration
>       (inherit config)
>       (substitute-urls
>         '("https://ci.guix.gnu.org"
>           "https://bordeaux.guix.gnu.org")))))
> ```
>

### Real-World Hardware: Using Nonguix for Laptops & Wi-Fi

By default, Guix System uses the 100% free **Linux-Libre** kernel. If you are running on modern ThinkPads, MacBooks, or gaming laptops with proprietary Intel/Realtek Wi-Fi and Bluetooth chips, you can use the **Nonguix** channel to declare the standard non-libre Linux kernel and firmware:
```scheme
;; Laptop configuration with Nonguix kernel and firmware
(use-modules (gnu)
             (nongnu packages linux)     ; From nonguix channel
             (nongnu system linux-initrd))

(operating-system
  (inherit %base-operating-system)
  (host-name "nomad-laptop")

  ;; Use vanilla Linux kernel with proprietary binary blob drivers
  (kernel linux)
  (initrd microcode-initrd)
  (firmware (list linux-firmware))

  ;; Automatically authorize the Nonguix pre-built substitute server!
  (services
    (modify-services %desktop-services
      (guix-service-type config =>
        (guix-configuration
          (inherit config)
          (substitute-urls
            (append (list "https://substitutes.nonguix.org")
                    %default-substitute-urls))
          (authorized-keys
            (append (list (local-file "/etc/nonguix-key.pub"))
                    %default-authorized-guix-keys)))))))
```

With this declaration, your laptop gets full hardware acceleration, functional Wi-Fi, and CPU microcode security patches without losing any of Guix System's declarative purity or atomic rollback powers!

### Applying the System: `guix system reconfigure`

To apply your changes, you execute:
```bash
sudo guix system reconfigure /etc/config.scm
```

When you run this command:

  - Guix instantiates and validates all Scheme definitions.
  - It builds all required store paths in `/gnu/store`.
  - It builds an entirely new operating system generation.
  - It signals the Shepherd init system to reload modified daemon configurations, spawn new services, and stop retired services.
  - It updates the GRUB bootloader menu with a new entry: **Generation $N+1$**.

### The Unbreakable Bootloader: GRUB Generations

What happens if you accidentally misconfigure your X server or build a kernel that kernel-panics on boot?

On other distributions, you are frantically reaching for a live USB stick and mounting partitions via `chroot`.

On Guix System, you simply reboot your machine. When the GRUB boot menu appears, you select:

**GNU Guix System — Generation 42 (Yesterday at 18:30)**

You hit `Enter`, and the system boots into the exact, known-working state of yesterday's operating system. 

> [!CAUTION]
> **😭 Tears of the Imperative Developer: The Broken Kernel Nightmare**
>
> Every veteran Linux user has an emotional scar from a bad kernel upgrade breaking their graphics drivers or Wi-Fi. In Guix System, an operating system update is never destructive. Every past system generation remains independently bootable in GRUB until you explicitly choose to garbage-collect it.

<div align="center">
  <img src="images/rollback_button.jpg" width="720" alt="Figure 6.1: The ultimate sysadmin superpower: When an experimental update catches fire, casually tap the GRUB Rollback button to rewind reality."/>
  <br/>
  <em>Figure 6.1: The ultimate sysadmin superpower: When an experimental update catches fire, casually tap the GRUB Rollback button to rewind reality.</em>
</div>

### Building Images: ISOs, VMs, and Cloud AMIs

Because your system is a pure Scheme function, Guix can transform your `config.scm` into any output format with a single command:
```bash
# 1. Build a bootable installation ISO image
guix system image -t iso9660 /etc/config.scm

# 2. Build a QEMU virtual machine image (QCOW2)
guix system image -t qcow2 /etc/config.scm

# 3. Build a Docker container image representing the complete OS
guix system image -t docker /etc/config.scm
```

[⬆ Back to Table of Contents](#-table-of-contents)



## Chapter 7: GNU Shepherd: The Lisp-Powered Init System

> *""Why should PID 1 be written in 1.5 million lines of C with twenty auxiliary binary utilities, when it could be written in elegant, functional Scheme?""*
> 
> — **The GNU Hacker Manifesto**

In the Linux world, few topics provoke as much religious fervor and flame wars as the init system. While the mainstream Linux ecosystem standardized on Systemd (a massive monolithic suite of daemons written in C and configured via thousands of INI files), GNU Guix chose a delightfully distinct path: **GNU Shepherd**.

Formerly known as `dmd` (*Daemon Managing Daemons*), the GNU Shepherd is an init system and service manager written entirely in **GNU Guile Scheme**.

### The Philosophy of Shepherd

The Shepherd's design philosophy is straightforward:

  - **PID 1 is a Guile REPL**: The process that initializes your computer and supervises your daemons is a Scheme interpreter.
  - **Services are First-Class Objects**: A service is not an opaque INI text file parsed by a custom grammar; it is a native Scheme record object with first-class start and stop closures.
  - **Minimalism & Transparency**: The core codebase of Shepherd is compact, readable, and easy to audit.

### Managing Services: The `herd` Command

To manage running system services, you interact with the `herd` command:
```bash
# List all running and stopped services
herd status

# Get detailed status and logs for a specific service
herd status ssh-daemon
herd status networking

# Start, stop, or restart a service
sudo herd stop ssh-daemon
sudo herd start ssh-daemon
sudo herd restart nscd

# View built-in documentation for a service
herd doc guix-daemon
```

> [!CAUTION]
> **😭 Tears of the Imperative Developer: INI Syntax Hell vs Scheme Functions**
>
> In systemd, if you want a custom pre-start check, you must learn thirty different directives like `ExecStartPre=`, `EnvironmentFile=`, `RuntimeDirectory=`, and escape quoting quirks.
>
> In Shepherd, a pre-start check is just a standard Scheme expression executed before spawning the process. You can check network interfaces, write files, or compute dynamic configuration files directly in pure Scheme.

### Writing a Custom Shepherd Service

How do you declare a custom daemon service in GNU Guix? You define a service using Shepherd's `make-forkexec-constructor`:
```scheme
;; Defining a custom background backup daemon service
(define my-backup-service
  (shepherd-service
    (provision '(my-backup-daemon))
    (requirement '(networking user-homes))
    (documentation "Runs an automated background data backup.")
    (start #~(make-forkexec-constructor
               (list #$(file-append rsync "/bin/rsync")
                     "-avz" "/var/data/" "backup.internal:/backups/")
               #:user "alice"
               #:group "users"
               #:log-file "/var/log/my-backup.log"))
    (stop #~(make-kill-destructor))
    (respawn? #t)))
```

Let us dissect this definition:

  - **`provision`**: The symbolic name of this service (what other services can depend on).
  - **`requirement`**: Services that must be started before this service can launch (in this case, `networking` and `user-homes`).
  - **`start`**: A G-Expression returning the execution constructor (`make-forkexec-constructor`).
  - **`stop`**: The destructor to gracefully terminate the process (`make-kill-destructor`).
  - **`respawn?`**: If `#t`, Shepherd will automatically restart the daemon if it crashes!

### Unprivileged User Services

You can also run your own personal GNU Shepherd instance inside your user session without root privileges:
```bash
# Start an unprivileged user shepherd
shepherd

# Manage user-level services (e.g. mpd, fetchmail, syncthing)
herd start syncthing
```

This integrates seamlessly with **Guix Home**, which we will explore in the next chapter.

[⬆ Back to Table of Contents](#-table-of-contents)



## Chapter 8: Guix Home: Declarative Dotfiles and Userland

> *""There are two kinds of developers: those whose dotfiles are a tangled web of broken symlinks in a forgotten GitHub repo, and those who use Guix Home.""*
> 
> — **The Unix Ascetic**

So far, we have seen how Guix manages package binaries and how Guix System manages the root operating system. But what about your personal home directory?

For decades, developers have managed their dotfiles (`.bashrc`, `.gitconfig`, `.config/nvim`, etc.) using ad-hoc shell scripts, GNU Stow symlink managers, or bare Git repositories. The result is almost always a brittle mess: symlinks point to deleted targets, local edits conflict with Git merges, and setting up a new laptop takes half a day of manual tinkering.

Enter **Guix Home**.

### The Philosophy of Guix Home

Guix Home applies the exact same declarative, functional paradigm of Guix System to your unprivileged `$HOME` directory:

  - Your user packages, environment variables, dotfiles, and user daemons are declared in a single Scheme file (`home-configuration.scm`).
  - Every update creates a new immutable **Home Generation**.
  - If an update breaks your shell or editor config, you can **roll back** your home environment instantly.
  - It works on **any** Linux distribution running GNU Guix, not just Guix System!

#### The Userland Paradox: Escaping `guix install` in `$HOME`

In [Chapter 6](#chapter-6-guix-system-one-file-to-rule-them-all), we established that system-wide packages must be declared in `/etc/config.scm`. However, many tools are personal: your preferred editor (Emacs, Neovim), CLI utilities (`ripgrep`, `fd`, `bat`), and shell customizations.

It is tempting to think: *"System daemons go into `/etc/config.scm`, but for my personal CLI tools, I will just run `guix install ripgrep` in my terminal as I learned in [Chapter 2](#chapter-2-daily-life-with-the-guix-cli)."*

**Do not fall into this trap!**

Running `guix install` recreates the exact problem of imperative mutable state inside your home directory. You get an untracked profile at `~/.guix-profile` with no version control, no Git history, and no way to reliably reproduce your developer setup on another machine without re-typing months of shell history.

**The recommended and idiomatic way to install user packages is declaratively through `home-configuration.scm`**. By declaring personal tools in your Guix Home configuration, your userland environment achieves the same mathematical reproducibility as the base operating system.

### Writing a `home-configuration.scm`

Let us inspect a complete, elegant `home-configuration.scm`:
```scheme
;; home-configuration.scm - Declarative personal userland
(use-modules (gnu home)
             (gnu home services)
             (gnu home services shells)
             (gnu home services version-control)
             (gnu packages)
             (gnu packages emacs)
             (gnu packages version-control)
             (gnu packages rust-apps)
             (guix gexp))

(home-environment
  ;; Packages to install in the user's home profile
  (packages (list emacs-no-x
                  git
                  ripgrep
                  fd
                  bat))

  ;; Services configuring dotfiles and user daemons
  (services
    (list
      ;; Declarative Bash Configuration
      (service home-bash-service-type
        (home-bash-configuration
          (guix-defaults? #t)
          (aliases '(("ll" . "ls -lha")
                     ("gs" . "git status")
                     ("gshell" . "guix shell --pure")))
          (bashrc (list (plain-file "bashrc-custom"
                          "export EDITOR=emacs\nexport HISTSIZE=50000\n")))))

      ;; Declarative Git Configuration (~/.gitconfig)
      (service home-git-service-type
        (home-git-configuration
          (user-name "Alice Hacker")
          (user-email "alice@example.org")
          (extra-config
            '((init ((defaultBranch . "main")))
              (pull ((rebase . #t)))
              (color ((ui . "auto")))))))

      ;; Deploying raw config files into ~/.config/
      (simple-service 'my-editor-config
        home-xdg-configuration-files-service-type
        `(("alacritty/alacritty.toml"
           ,(local-file "configs/alacritty.toml")))))))
```

#### Installing User Packages Declaratively

Look at lines 40–45 in the configuration above. This `packages` field is where all your everyday personal applications and developer tools are installed:
```scheme
;; Packages to install in the user's home profile
  (packages (list emacs-no-x
                  git
                  ripgrep
                  fd
                  bat))
```

Whenever you need a new tool in your daily workflow:

  - Open your `home-configuration.scm`.
  - Add the package to the `packages` list (making sure its module is imported at the top).
  - Run `guix home reconfigure home-configuration.scm`.

No `sudo` is needed. Guix builds or fetches the packages, links them into your active home profile at `~/.guix-home/profile/bin`, and creates an immutable new generation. If you decide a tool is cluttering your environment, simply remove it from the list and reconfigure.

### Applying Your Home Configuration

To instantiate or update your home environment, you simply run:
```bash
guix home reconfigure home-configuration.scm
```

When you run this command:

  - Guix validates your Scheme records.
  - It generates the necessary configuration files and places them immutably in `/gnu/store`.
  - It atomically updates symlinks in `~/.config/` and your home directory.
  - It creates a new Home Generation in `~/.guix-home`.

### Navigating Home Generations and Rollbacks

Did you make an experimental edit to your shell configuration that broke your terminal startup?
```bash
# List all historical generations of your home environment
guix home list-generations

# Roll back to the previous home generation in 2 milliseconds
guix home roll-back

# Switch directly to Generation 5
guix home switch-generation 5
```

> [!CAUTION]
> **😭 Tears of the Imperative Developer: The New Laptop Onboarding Experience**
>
> On traditional systems:
> 
>   - Buy new laptop.
>   - Spend 6 hours installing packages, copying SSH keys, cloning 14 git repos, debugging Python versions, and configuring shell themes.
> 
> With Guix Home:
> 
>   - Buy new laptop. Install GNU Guix.
>   - Clone your `home-configuration.scm`.
>   - Run `guix home reconfigure home-configuration.scm`.
>   - In 45 seconds, your entire personalized computing environment is bit-for-bit identical to your previous machine.
> 

### The Grand Architecture: The Three Declarative Tiers

Having explored both Guix System and Guix Home, the overarching vision of GNU Guix becomes unmistakable. Package management is not a sequence of ad-hoc terminal mutations; it is a layered, declarative architecture:

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: The Three Tiers of Package Management in GNU Guix**
>
> 
>   - **Tier 1: System-Wide Declarative (`/etc/config.scm`)**:
>   
>     - *Tool*: `sudo guix system reconfigure /etc/config.scm`
>     - *Target*: Linux kernel, system daemons, core fonts, certificates, display managers, virtualization.
>     - *Scope*: Entire machine, managed by the administrator.
>   
>
>   - **Tier 2: Userland Declarative (`home-configuration.scm`)**:
>   
>     - *Tool*: `guix home reconfigure home-configuration.scm`
>     - *Target*: Personal CLI tools, editors, terminal emulators, shell aliases, dotfiles, user daemons.
>     - *Scope*: Personal `$HOME`, requiring zero root permissions. Works on Guix System **and** foreign distributions!
>   
>
>   - **Tier 3: Ephemeral & Project Declarative (`manifest.scm` & `guix shell`)**:
>   
>     - *Tool*: `guix shell` or `guix shell -m manifest.scm`
>     - *Target*: Project-specific dependencies, compilers, libraries, temporary debugging sessions.
>     - *Scope*: Isolated to the current shell or project directory; zero permanent disk pollution.
>   
> 

Where does the imperative `guix install` from [Chapter 2](#chapter-2-daily-life-with-the-guix-cli) fit into this picture? It serves as an emergency spare tire: a quick, familiar mechanism for users on foreign distributions who want to test a tool for five minutes without updating a configuration file. But for everything you rely on daily, **declaring your environment in Scheme code is what delivers the holy grail of computing: 100% mathematical reproducibility**.

[⬆ Back to Table of Contents](#-table-of-contents)



---

# Part IV: The Master Craftsman — Packaging with Scheme



## Chapter 9: The Anatomy of a Package: `(define-public ...)`

> *""In other operating systems, writing a package recipe involves writing 300 lines of arcane Bash scripts and cryptic SPEC files. In Guix, it is an elegant mathematical declaration in Scheme.""*
> 
> — **The GNU Guix Contributor Guide**

At the heart of GNU Guix is the package definition. A package in Guix is not a script that gets run blindly; it is a first-class **Scheme record object** that formally describes the inputs, source code, build system, and metadata required to produce an immutable store path.

### A Complete Package Recipe from Scratch

Let us examine a real-world, complete package definition for a fictional modern C/C++ tool called `fast-grep`:
```scheme
(define-module (my-channel packages fast-grep)
  #:use-module (guix packages)
  #:use-module (guix download)
  #:use-module (guix git-download)
  #:use-module (guix build-system cmake)
  #:use-module ((guix licenses) #:prefix license:)
  #:use-module (gnu packages compression)
  #:use-module (gnu packages pcre)
  #:use-module (gnu packages pkg-config)
  #:use-module (gnu packages check))

(define-public fast-grep
  (package
    (name "fast-grep")
    (version "1.4.2")
    (source
      (origin
        (method git-fetch)
        (uri (git-reference
               (url "https://github.com/example/fast-grep")
               (commit (string-append "v" version))))
        (file-name (git-file-name name version))
        (sha256
          (base32
            "0n62f928z11j4p2q19r345c2x48k631k1v38d4a9v18z0147f9lm"))))
    (build-system cmake-build-system)
    (arguments
      '(#:configure-flags '("-DENABLE_AVX2=ON"
                           "-DBUILD_SHARED_LIBS=ON")
        #:tests? #t))
    (native-inputs
      (list pkg-config
            googletest))
    (inputs
      (list zlib
            pcre2))
    (home-page "https://example.org/fast-grep")
    (synopsis "Blazingly fast parallel regular expression search tool")
    (description
      "Fast-Grep is a high-performance multithreaded regex search tool
designed to traverse vast directory trees.  It leverages PCRE2 and AVX2
vector instructions for near-instantaneous indexing.")
    (license license:gpl3+)))
```

### Deconstructing the Package Fields

Let us dissect the crucial components of this definition:

#### 1. Source and Integrity (`origin`)

Guix requires the source code to be cryptographically verified:

  - **`method`**: Can be `url-fetch` (for tarballs) or `git-fetch` (for Git repositories).
  - **`sha256`**: The expected cryptographic checksum in Nix-base32 format. If the upstream repository changes even a single whitespace character in a release, the hash will not match and Guix will abort the build with a security violation.

> [!TIP]
> **💡 Guix Wizard Pro-Tip: Computing Source Hashes**
>
> You don't need to guess hashes! Use Guix's built-in hashing tools:

> ```bash
> # Download a tarball and output its base32 hash:
> guix download https://example.org/tarball-1.0.tar.gz
> 
> # Compute the base32 hash of a local git checkout or directory:
> guix hash -rx ./my-git-clone/
> ```
>

#### 2. The Build System (`build-system`)

Guix provides dozens of pre-configured build systems that encode the standard conventions of various ecosystems:

  - `gnu-build-system`: For traditional `./configure`, `make`, and `make install`.
  - `cmake-build-system`: For CMake-based C/C++ projects.
  - `python-build-system`: For standard Python packages (`setup.py` and PEP 517/518).
  - `cargo-build-system`: For Rust crates and binaries.
  - `go-build-system`: For Go modules and packages.
  - `meson-build-system`: For Meson/Ninja based software.

#### 3. Input Classification: The Golden Rule

Guix makes a strict, critical distinction between three types of inputs:

| **Input Type** | **Purpose and Behavior** |
| :--- | :--- |
| **`inputs`** | Libraries and runtime dependencies compiled for the **target architecture** (e.g., `zlib`, `openssl`). Embedded into the final binary via RUNPATH. |
| **`native-inputs`** | Tools and compilers executed on the **build host machine** during compilation (e.g., `pkg-config`, `gcc`, test frameworks like `googletest`). Not needed at runtime when cross-compiling! |
| **`propagated-inputs`** | Dependencies that must be automatically pulled into the user's profile whenever this package is installed (e.g., Python runtime library dependencies or C header files required by a library's public API). |

*The Three Classes of Package Inputs in GNU Guix*

> [!WARNING]
> **⚠️ Caution: Footgun Detected!: The Propagated Inputs Trap**
>
> Do NOT use `propagated-inputs` unless absolutely necessary! Overusing propagated inputs pollutes user profiles with transitive dependencies and re-introduces the collision risks of traditional package managers. Use standard `inputs` whenever possible.

### Instant Importers: `guix import`

Don't want to write package recipes by hand from scratch? Guix comes with automatic importers for almost every major language ecosystem:
```bash
# Import a Python package from PyPI
guix import pypi requests

# Import an R package from CRAN
guix import cran ggplot2

# Import a Rust crate from crates.io (recursively importing dependencies!)
guix import crate --recursive ripgrep

# Import a Go module
guix import go github.com/schollz/croc
```

The importer connects to the upstream API, downloads the metadata and checksums, resolves dependencies, and prints out a pristine, syntactically valid Guile Scheme package recipe directly into your terminal!

[⬆ Back to Table of Contents](#-table-of-contents)



## Chapter 10: Build Phases, G-Expressions, and Shebangs

> *""In ordinary programming, you write code that runs now. In Guix packaging, you write Scheme code that constructs Scheme code that will run in an isolated chroot sandbox tomorrow on another machine.""*
> 
> — **The Wizard of G-Expressions**

Most software projects build cleanly with standard flags. But occasionally, you will encounter upstream software that commits unforgivable sins: hardcoding `/bin/bash`, expecting files to exist in `/usr/share`, failing test suites because network access is disabled, or requiring complex wrapper scripts to set environment variables.

To tame these unruly packages, GNU Guix gives you two formidable tools: **Phase Modification** and **G-Expressions**.

### The Build Phase Pipeline

Every build system in Guix executes a sequential pipeline of **Phases**. For example, the `gnu-build-system` runs:

  - `unpack`: Extracts the source tarball or git archive.
  - `patch-source-shebangs`: Replaces hardcoded `/bin/sh` with the store path of GNU Bash.
  - `configure`: Runs `./configure` with appropriate `–prefix=/gnu/store/...` flags.
  - `build`: Runs `make -j N`.
  - `check`: Runs the automated test suite (`make check`).
  - `install`: Runs `make install`.
  - `patch-shebangs`: Replaces shebangs in installed scripts.
  - `strip`: Strips debug symbols (unless requested).
  - `validate-runpath`: Verifies that all dynamic ELF libraries point to valid `/gnu/store` paths.

### Modifying Phases with `modify-phases`

You can intercept, alter, delete, or inject custom Scheme code at any point in this pipeline using the `modify-phases` macro:
```scheme
(arguments
  (list
    #:phases
    #~(modify-phases %standard-phases
        ;; 1. Delete a phase (e.g. if tests require internet)
        (delete 'check)

        ;; 2. Add a custom phase before 'configure
        (add-before 'configure 'set-environment-flags
          (lambda _
            (setenv "C_INCLUDE_PATH"
                    (string-append #$(this-package-input "zlib") "/include"))))

        ;; 3. Replace a phase entirely
        (replace 'build
          (lambda* (#:key (make-flags '()) (#:allow-other-keys))
            (apply invoke "make" "all-optimized" make-flags)))

        ;; 4. Add a custom wrapper phase after 'install
        (add-after 'install 'wrap-executable
          (lambda* (#:key outputs #:allow-other-keys)
            (let* ((out (assoc-ref outputs "out"))
                   (bin (string-append out "/bin/my-app")))
              (wrap-program bin
                `("PATH" ":" prefix
                  (,(string-append #$(this-package-input "coreutils") "/bin"))))))))))
```

### The Glory of G-Expressions (`#\~{}` and `#$`)

Why are there funny characters like `#\~{}` and `#$` in modern Guix code?

In Guix, code is divided into two distinct worlds:

  - **Host-side Code**: Evaluated on your current machine when calculating the derivation graph.
  - **Build-side Code**: Evaluated inside the isolated build daemon sandbox when actually compiling the package.

**G-Expressions (G-Exps)** provide a type-safe, hygienic mechanism for staging code that will be executed in the build sandbox:

  - **`#\~{}`** (*G-Exp Quoting*): Begins a staged code block to be sent to the builder.
  - **`#$`** (*Ungexp*): Unquotes an object from the host environment, resolving packages to their exact `/gnu/store/...` paths!
  - **`#$@`** (*Ungexp-Splicing*): Unquotes and splices a list of items into the staged code.

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: The Magic of `#$(file-append ...)`**
>
> When you write:

> ```scheme
> #$(file-append bash "/bin/sh")
> ```
>
> Guix automatically:
> 
>   - Records a build-time and runtime dependency on the `bash` package.
>   - During derivation expansion, replaces the expression with the exact immutable store path:
>
>   `/gnu/store/12345...-bash-5.1.16/bin/sh`
>
> 
> You never have to hardcode or guess store paths!

### The Battle Against Hardcoded Paths and Shebangs

The single most common bug in porting software to Guix is an upstream script with a header like `#!/bin/bash` or `#!/usr/bin/env python3`.

Remember: In Guix, **`/bin/bash` does not exist!** (There is only `/bin/sh` for POSIX compatibility on Guix System).

> [!WARNING]
> **⚠️ Caution: Footgun Detected!: The Missing Shebang Gotcha**
>
> If an installed script has `#!/usr/bin/python`, executing it will result in the infamous:

> ```bash
> bash: ./my-script.py: No such file or directory
> ```
>
> The kernel is telling you that the interpreter binary named in the shebang line does not exist on the filesystem.

Guix provides `patch-shebangs` automatically, but for dynamically invoked scripts or custom build steps, you can resolve binaries cleanly using `search-input-file`:
```scheme
(lambda* (#:key inputs outputs #:allow-other-keys)
  (let ((bash (search-input-file inputs "/bin/bash"))
        (sed  (search-input-file inputs "/bin/sed")))
    (substitute* "generate-data.sh"
      (("/bin/bash") bash)
      (("/usr/bin/sed") sed))))
```

With `substitute*` and `search-input-file`, even the most stubborn legacy codebase can be brought into pristine functional compliance.

[⬆ Back to Table of Contents](#-table-of-contents)



## Chapter 11: Rolling Your Own Custom Channel

> *""Give a developer a package, and you feed them for a day. Teach a developer to write a Guix channel, and their entire team never suffers from dependency issues again.""*
> 
> — **The Ancient Guild of Guixers**

Once you start writing your own Guix package definitions, you will quickly want to share them with your colleagues, your organization, or the broader world.

Rather than emailing `.scm` files around or maintaining fragile private PPA repositories, GNU Guix allows anyone to turn any Git repository into an authenticated, first-class **Guix Channel**.

### The Anatomy of a Channel Repository

A custom channel is simply a Git repository structured with standard Scheme module paths. Here is a recommended layout:
```bash
my-guix-channel/
|-- .guix-channel          # Channel metadata file
|-- etc/
|   \-- news.txt           # Announcements displayed on `guix pull`
\-- mychannel/
    |-- packages/
    |   |-- web.scm        # Web applications & services
    |   \-- science.scm    # Scientific computation packages
    \-- services/
        \-- custom.scm     # Custom Shepherd system services
```

### The `.guix-channel` Metadata File

At the root of your repository, create a `.guix-channel` file:
```scheme
;; .guix-channel
(channel
  (version 0)
  (directory ".")
  ;; Optional: Declare channel dependencies
  (dependencies
    (list (channel
            (name 'guix)
            (url "https://git.savannah.gnu.org/git/guix.git")))))
```

### Writing Package Modules Inside the Channel

In `mychannel/packages/science.scm`, declare your module matching the directory path:
```scheme
(define-module (mychannel packages science)
  #:use-module (guix packages)
  #:use-module (guix download)
  #:use-module (guix build-system gnu)
  #:use-module ((guix licenses) #:prefix license:))

(define-public custom-simulator
  (package
    (name "custom-simulator")
    (version "2.0.0")
    (source (origin
              (method url-fetch)
              (uri "https://internal.example.org/sim-2.0.0.tar.gz")
              (sha256
               (base32
                "0123456789abcdef0123456789abcdef0123456789abcdef0123"))))
    (build-system gnu-build-system)
    (synopsis "Proprietary internal physics simulation engine")
    (description "High performance simulator for organizational workflows.")
    (home-page "https://internal.example.org")
    (license license:gpl3+)))
```

### Testing Your Channel Locally: `-L`

Before committing and pushing your channel to Git, you can test your new packages immediately using the `-L` (load path) flag:
```bash
# Build the package directly using the local channel directory
guix build -L /path/to/my-guix-channel custom-simulator

# Test running the package in a containerized shell
guix shell -L /path/to/my-guix-channel custom-simulator -- custom-simulator --version
```

### Channel News: `etc/news.txt`

Guix provides a built-in notification system. When users of your channel run `guix pull`, Guix will display formatted news items for new releases or breaking changes:
```scheme
(channel-news
  (version 0)
  (entry (tag "v2.0.0")
         (title (en "Major upgrade: Custom Simulator 2.0 Released!"))
         (body (en "Version 2.0 introduces GPU acceleration and fixes memory leaks."))))
```

> [!TIP]
> **💡 Guix Wizard Pro-Tip: Subscribing Teammates to Your Channel**
>
> To enable your team to use your new channel, they simply add this snippet to their `~/.config/guix/channels.scm`:

> ```scheme
> (cons (channel
>         (name 'mychannel)
>         (url "https://git.example.org/my-guix-channel.git")
>         (branch "main"))
>       %default-channels)
> ```
>
> After running `guix pull`, your entire company's internal software library is available directly via `guix install` and `guix shell`!

[⬆ Back to Table of Contents](#-table-of-contents)



---

# Part V: The Real-World Frontier — Deployment, Domains & Pragmatic Hardware



## Chapter 12: Standalone Bundles: `guix pack` for Docker, AppImage, and HPC

> *""The true test of a reproducible deployment is not whether it runs on your machine, but whether it runs on an ancient Red Hat 7 cluster managed by sysadmins who forbid root access, disable internet connectivity, and refuse to install Guix.""*
> 
> — **The HPC Vagabond**

Up to this point in our journey, we have enjoyed the paradise of having GNU Guix installed on our systems. Whether managing user profiles, spawning disposable `guix shell` containers, or declaring our entire workstation via Guix System, the `guix-daemon` and the immutable store (`/gnu/store`) were always there to orchestrate reality.

> [!CAUTION]
> **😭 Tears of the Imperative Developer: The Real-World Transfer Dilemma**
>
> What happens when you need to deploy your software to:
> 
>   - A corporate cloud Kubernetes cluster where nodes only accept Docker or OCI container images?
>   - A massive institutional High-Performance Computing (HPC) supercomputer with thousands of nodes running CentOS 7 or RHEL 8, where sysadmins strictly forbid root access, block outbound internet access, and refuse to install GNU Guix?
>   - A colleague's vanilla Ubuntu or Fedora laptop where they just want a single, zero-dependency executable they can double-click or run from the terminal without installing Guix?
> 

Traditional answers to this problem are depressing: you either write a 60-line, non-reproducible `Dockerfile` that pulls mutable APT mirrors and `pip` wheels, or you spend days fighting dynamic linker errors (`version `GLIBC_2.34' not found`) trying to build static binaries.

GNU Guix offers a revolutionary escape hatch: `guix pack`.

### The Philosophy of `guix pack`

In Guix, every package in `/gnu/store` is already a self-contained, immutable artifact whose complete dependency graph is known to the byte. 

Because Guix calculates the exact **closure** (the target package plus every single shared library, interpreter, data file, configuration script, and runtime dependency it requires), Guix can extract that sub-graph from `/gnu/store` and pack it into whatever standalone format the outside world demands:

  - **Standalone Tarballs (`-f tar`)**: Unpack anywhere, with optional execution wrappers.
  - **Docker / OCI Images (`-f docker`)**: Layered, bit-for-bit reproducible container images with zero base-OS bloat.
  - **AppImage Bundles (`-f appimage`)**: Single-file executables with embedded squashfs runtimes for any Linux desktop.
  - **Debian / RPM Packages (`-f deb`, `-f rpm`)**: Standard system packages containing the relocatable Guix closure for legacy server fleets.
  - **SquashFS Images (`-f squashfs`)**: Read-only compressed images ideal for Singularity, Apptainer, and HPC network filesystems.

Crucially, **Guix does not need Docker to build Docker images**, nor does it need AppImage toolkits or Debian build tools. It creates all of these archives directly from the store graph with bit-for-bit reproducibility.

### The Relocatability Miracle: How Non-Guix Systems Run Store Binaries

There is an obvious technical hurdle: binaries compiled by Guix have their runtime library paths (`RUNPATH`) hardcoded to absolute paths inside `/gnu/store/...`. 

If you copy these binaries to a machine that does not have `/gnu/store` mounted, any attempt to launch them fails immediately with:

`bash: ./bin/python3: No such file or directory`

The Linux dynamic linker (`ld-linux.so`) cannot find its interpreter at `/gnu/store/...`!

How does `guix pack` solve this without requiring root access on the target machine? It provides three distinct **relocation wrappers** via the `-R` (or `–relocatable`) flag:

#### 1. User Namespaces (The Default)

On modern Linux kernels (version 3.10+), an unprivileged user can create a mount namespace (using the `clone(2)` or `unshare(2)` system calls). 
When you invoke a relocatable binary produced with `guix pack -R`, a lightweight C launcher executes first. It creates an unprivileged user and mount namespace, mounts the unpacked directory onto a virtual `/gnu/store` visible only to that process tree, and executes the target program. To the application, `/gnu/store` exists perfectly, while the host filesystem remains untouched!

#### 2. PRoot Fallback

Some hardened institutional clusters or older Linux kernels disable unprivileged user namespaces (`kernel.unprivileged_userns_clone = 0`). In this scenario, the wrapper automatically falls back to **PRoot** (which intercepts filesystem system calls via `ptrace(2)` to translate `/gnu/store` accesses transparently in user space).

#### 3. Fakechroot Fallback

As a final lightweight fallback, Guix can employ an `LD_PRELOAD` wrapper that intercepts standard C library file functions.

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: The Execution Ladder**
>
> By passing `–relocatable` (or `-R`), Guix generates binaries that try:
>
> **User Namespaces** → (fallback) → **PRoot**
>
> Your package will run on virtually **any** Linux machine from the past 15 years, unprivileged, without installing Guix or Docker!

### Packaging for High-Performance Computing (HPC)

HPC clusters represent the most common battleground for relocatable bundles. Imagine you have built a complex computational pipeline using Python, NumPy, SciPy, and OpenMPI. The target cluster runs Red Hat Enterprise Linux 7 with no internet access and no Guix.

#### Building a Self-Contained Tarball

Let us package Python and your analysis tools into a standalone, relocatable tarball:
```bash
# Generate a relocatable tarball with symlinks for convenient execution
guix pack -R \
  -S /bin=bin \
  -S /lib=lib \
  -S /share=share \
  python python-numpy python-scipy \
  -C xz
```

Let us dissect the flags:

  - `-R` (or `–relocatable`): Wraps all executables with the user-namespace / PRoot relocation launcher.
  - `-S /bin=bin`: Creates a top-level `bin/` symlink pointing to the profile's `bin/` directory inside the archive. This ensures you can unpack and immediately run `./bin/python3`.
  - `-C xz`: Compresses the output archive using XZ (options include `gzip`, `bzip2`, `zstd`, `none`).

Guix builds the closure, assembles the archive, and prints the path of the generated tarball:

`/gnu/store/3x9k1p...-tarball-pack.tar.xz`

#### Deploying and Running on the HPC Cluster

Now, transfer this tarball to the remote supercomputer using `scp` or an external drive:
```bash
# On your local Guix workstation:
scp /gnu/store/3x9k1p...-tarball-pack.tar.xz user@cluster.hpc.edu:~/

# On the remote supercomputer (which has NO Guix installed):
ssh user@cluster.hpc.edu
mkdir -p ~/my-env && cd ~/my-env
tar -xf ~/3x9k1p...-tarball-pack.tar.xz

# Execute immediately without root permissions!
./bin/python3 -c "import numpy, scipy; print('HPC Success with NumPy', numpy.__version__)"
```

Notice what just happened: the cluster node has no `/gnu/store`, no internet access, and ancient system libraries. Yet Python, NumPy, OpenBLAS, and GCC runtime libraries executed flawlessly in user space!

#### Submitting SLURM Batch Jobs

You can directly submit your relocatable bundle in SLURM or PBS/Torque batch submission scripts:
```bash
#!/bin/bash
#SBATCH --job-name=guix_sim
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=16
#SBATCH --time=12:00:00

# Execute simulation using our unpacked relocatable Guix environment
~/my-env/bin/python3 ~/scripts/distributed_simulation.py --input /data/raw.h5
```

### Direct Store Transfers: `guix copy` and `guix archive`

If the remote machine or cluster *does* have GNU Guix installed (such as a cluster where sysadmins run the `guix-daemon`), you do not even need to pack tarballs. You can beam store items directly across SSH connections.

#### Zero-Friction Transfer with `guix copy`

`guix copy` transfers a package and its complete closure over an SSH pipe directly into the remote daemon's store:
```bash
# Copy the entire closure of R and Bioconductor to the remote cluster
guix copy --to=user@cluster.hpc.edu r r-deseq2

# Or pull an environment built on a fast build farm down to your local laptop
guix copy --from=builder.internal.net /gnu/store/8j29...-large-model
```

Because Guix checks store hashes on both sides, it transfers **only the missing store items**! If the remote machine already has GLIBC and Python, `guix copy` only beams over the delta.

#### Air-Gapped Transfers with `guix archive`

For military, medical, or secure air-gapped systems that are physically disconnected from the internet and have no SSH access:
```bash
# 1. Export package closure to an authenticated binary archive file
guix archive --export -r python python-pytorch > pytorch-closure.nar

# 2. Walk the USB drive across the air-gap to the secure facility

# 3. Import directly into the secure machine's Guix store
guix archive --import < pytorch-closure.nar
```

The archive is cryptographically signed with your private key and authenticated by the recipient machine's authorized keys.

### Docker and OCI Images Without Docker: `-f docker`

Traditional `Dockerfile` workflows are an operational nightmare:
```bash
# The Traditional Anti-Pattern: Fragile, non-reproducible, bloated
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip curl gcc \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install torch torchvision --extra-index-url https://...
COPY . /app
CMD ["python3", "/app/server.py"]
```

This Dockerfile violates every tenet of engineering reliability:

  - **Non-reproducible**: Running this tomorrow pulls different Ubuntu security patches and different `pip` wheels.
  - **Bloated**: You ship a package manager (`apt`), systemd stubs, man pages, documentation, and build caches you will never use in production.
  - **Privileged Daemon**: Building requires the Docker daemon running with root privileges on the host.

#### Building a Minimal Docker Image with `guix pack`

With `guix pack`, Guix constructs the Docker image archive directly from its dependency graph without running Docker:
```bash
# Generate an ultra-lean, reproducible Docker image
guix pack -f docker \
  -S /bin=bin \
  -S /lib=lib \
  --entry-point=bin/guile \
  guile
```

Let us examine a real-world web microservice example packaging Python, Uvicorn, and a REST API:
```bash
guix pack -f docker \
  -S /bin=bin \
  -S /etc=etc \
  --entry-point=bin/uvicorn \
  python python-uvicorn python-fastapi nss-certs
```

<div align="center">
  <img src="images/guix_pack_diagram.jpg" width="720" alt="Figure 12.1: From pure Scheme store graph to production: `guix pack` producing bit-for-bit identical Docker, AppImage, and HPC tarballs with zero host dependencies."/>
  <br/>
  <em>Figure 12.1: From pure Scheme store graph to production: `guix pack` producing bit-for-bit identical Docker, AppImage, and HPC tarballs with zero host dependencies.</em>
</div>

#### Loading and Running in Docker / Podman

The resulting `.tar.gz` file is a valid OCI/Docker image. You can load and run it on any Kubernetes cluster, AWS ECS, or local Docker daemon:
```bash
# Load image into Docker or Podman
docker load < /gnu/store/7q8m...-docker-pack.tar.gz

# Inspect image size and history
docker images
# REPOSITORY          TAG                 IMAGE ID            SIZE
# guile-fastapi       latest              4f8c9b2a1e0d        82.4MB

# Run the container
docker run -p 8000:8000 guile-fastapi:latest
```

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: Why Guix Docker Images Are Superior**
>
> 
>   - **Bit-for-Bit Reproducible**: Two developers compiling the same package commit with `guix pack -f docker` generate Docker images with the exact same SHA-256 image ID!
>   - **Attack Surface Reduction**: There is no `/bin/sh`, no package manager, no compiler, and no unnecessary binaries inside the container unless you explicitly declare them. If an attacker discovers an injection vulnerability, there are no shells or system utilities to exploit!
>   - **Minimal Footprint**: A Guix-built Python microservice image often weighs 60MB, compared to 850MB for standard Debian-based Python images.
> 

### Single-File Desktop Apps: `-f appimage`

Desktop Linux distribution has long suffered from packaging fragmentation. An Ubuntu user wants a `.deb`, a Fedora user wants an `.rpm`, an Arch user wants a PKGBUILD, and someone on an older openSUSE release cannot run your app because their system libraries are too old.

The **AppImage** format packages an application and its runtime dependencies into a single executable file that runs on any modern desktop Linux distribution.

`guix pack` can build AppImages out of the box:
```bash
# Package the Inkscape vector graphics editor into a standalone AppImage
guix pack -f appimage \
  -S /bin=bin \
  --entry-point=bin/inkscape \
  inkscape
```

Or package a lightweight text editor or custom tool:
```bash
# Package a terminal editor into an executable AppImage
guix pack -f appimage \
  -S /bin=bin \
  --entry-point=bin/nano \
  nano
```

The output is an executable AppImage file:
```bash
# Make executable and run anywhere:
chmod +x /gnu/store/6v4k...-nano-appimage
./gnu/store/6v4k...-nano-appimage
```

You can copy this file to a USB flash drive, email it to a colleague on Linux Mint or Ubuntu, and they can double-click and run it instantly. No installation, no PPA repositories, no root privileges, and no dynamic linker errors!

### Packing from Manifests and Channels

Just like `guix shell`, `guix pack` seamlessly accepts `-m manifest.scm` and combines with `guix time-machine`.

#### 1. Packing from a Project `manifest.scm`

Instead of listing individual packages on the command line, you can pack an entire development or production manifest:
```scheme
;; prod-manifest.scm
(specifications->manifest
  '("python"
    "python-scipy"
    "python-pandas"
    "python-scikit-learn"
    "nss-certs"))
```

Pack this manifest directly into a relocatable tarball or Docker image:
```bash
# Pack the entire manifest into a production Docker image
guix pack -f docker -m prod-manifest.scm -S /bin=bin
```

#### 2. Time-Traveling Docker Builds

Combine `guix time-machine` and `guix pack` to generate bit-for-bit identical Docker or HPC bundles from a pinned historical state:
```bash
# Build a Docker container using the exact package graph from 2024
guix time-machine -C channels.scm -- \
  pack -f docker \
  -m prod-manifest.scm \
  -S /bin=bin
```

This is the holy grail of DevOps and scientific computing: a pipeline that can rebuild a bit-for-bit identical production Docker container 5 years from now, completely offline, from source, without relying on external Docker registries or third-party package mirrors.

### Summary: Choosing the Right Deployment Vehicle

| **Format** | \textbf{Flag \ | Options} | **Best For** |
| :--- | :--- | :--- | :--- |
| **Relocatable Tarball** | `-R -S /bin=bin -C xz` | HPC clusters, unprivileged shared servers, no Guix or root |  |
| **Docker / OCI** | `-f docker –entry-point=...` | Kubernetes, cloud deployments, microservices |  |
| **AppImage** | `-f appimage –entry-point=...` | Desktop applications, non-technical Linux end-users |  |
| **SquashFS** | `-f squashfs` | Singularity / Apptainer on HPC network filesystems |  |
| **Guix Copy** | `guix copy –to=host pkg` | Machines with Guix installed, delta-only SSH synchronization |  |
| **Guix Archive** | `guix archive –export pkg` | Air-gapped secure installations, offline backups |  |

With `guix pack`, you no longer have to convince your company or your university HPC administrators to install GNU Guix before you can reap the rewards of functional reproducibility. You can build in the clean, principled haven of Guix, and distribute to the messy outside world in whatever container or archive format it demands.

[⬆ Back to Table of Contents](#-table-of-contents)



## Chapter 13: Guix in the Wild: Domain Impact and Taming Real Hardware with Nonguix

> *""In theory, there is no difference between theory and practice. In practice, your laptop's Wi-Fi card requires a proprietary binary blob, your university cluster has no root access, and your computational biology pipeline broke because an R package updated at midnight.""*
> 
> — **The Pragmatic Guix Alchemist**

So far, we have explored GNU Guix from the perspective of computer science elegance: immutable stores, mathematical functions, declarative operating systems, and Scheme macros. But how does this functional paradigm fare when thrown into the messy, chaotic, real world?

In this chapter, we explore two transformative aspects of Guix in the wild:

  - **Domain Impact**: How Guix is revolutionizing High-Performance Computing (HPC), bioinformatics, artificial intelligence, and academic research.
  - **Pragmatic Hardware with Nonguix**: How to tame consumer laptops, proprietary Wi-Fi chips, NVIDIA GPUs, and non-free software without sacrificing a single drop of declarative purity.

### Guix in Science & Industry: The Reproducibility Revolution

#### 1. High-Performance Computing (HPC) & Supercomputing

If you have ever used an institutional supercomputer or shared HPC cluster, you know the traditional pain:

  - You do not have `sudo` permissions (for good reason).
  - The cluster runs an ancient distribution (like Red Hat Enterprise Linux 7 or CentOS) with GCC versions from a decade ago.
  - You need bleeding-edge MPI libraries, specific CUDA toolkits, and dozens of custom packages.
  - Traditional solutions like Environment Modules or Conda pollute paths, fail to isolate dynamic libraries, and break when compute nodes have slight architectural drifts.

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: Unprivileged Cluster Freedom with Guix HPC**
>
> Because GNU Guix package management is entirely unprivileged:
> 
>   - Cluster sysadmins install the `guix-daemon` once.
>   - Hundreds of researchers can independently install, upgrade, and mix conflicting software stacks in their own profiles without ever filing an IT helpdesk ticket!
>   - Guix integrates natively with **SLURM**, allowing researchers to run batch jobs with `guix shell –container –manifest=manifest.scm – srun ./simulation`.
> 

Leading research institutes—such as Inria in France, the Max Delbr\"uck Center in Germany, and the University of Tennessee—now manage multi-petaflop clusters powered by Guix HPC.

#### 2. Bioinformatics & Computational Biology

Bioinformatics pipelines are notorious for being the most fragile software ecosystems on the planet. A typical genomic pipeline might combine:

  - 40 different command-line tools written in C, C++, and Fortran.
  - 25 Python packages with pinned C extensions.
  - 150 R packages from CRAN and Bioconductor.
  - A workflow engine like Nextflow or Snakemake.

A single minor version bump in an underlying alignment library can silently change variant calling results, leading to retracted scientific papers and millions of wasted research dollars.

With GNU Guix, bioinformaticians define their complete software environment in a single `manifest.scm` and pin the exact channel commits with `channels.scm`. Ten years later, any laboratory on Earth can re-run that pipeline with bit-for-bit identical results.

> [!CAUTION]
> **😭 Tears of the Imperative Developer: The Replication Crisis in Computational Science**
>
> In 2019, a major study attempted to reproduce the computational analysis of over 400 published machine learning and bioinformatics papers. Less than 25% could be re-executed because of missing dependencies, changed numerical libraries, and unstated build flags.
>
> Guix transforms reproducibility from an aspirational dream into an automated mathematical guarantee.

#### 3. Data Science, Machine Learning & AI

Modern AI engineering often feels less like programming and more like wrestling with dynamic linker errors:

`ImportError: libcudart.so.11.0: cannot open shared object file`

Between CUDA versions, CuDNN drivers, Python wheels compiled against conflicting GLIBC versions, and PyTorch/TensorFlow bindings, ML developers frequently resort to 15GB monolithic Docker containers that nobody knows how to rebuild from source.

The **Guix Science** channel provides cleanly packaged, transparently built PyTorch, JAX, and CUDA/ROCm stacks where every GPU acceleration library is explicitly tracked in the dependency graph.

#### 4. Verifiable Software Supply Chains (SLSA Level 4)

In enterprise software engineering, security attacks on the build pipeline (such as the SolarWinds compromise) have made verifiable builds a critical priority.

Because Guix builds are **hermetic**, timestamp-independent, and isolated from host impurities, Guix achieves industry-leading **Bootstrappable and Reproducible Builds**:

  - You can independently compile a package on three different machines across the world and verify that they produce the exact, bit-for-bit identical SHA-256 binary hash.
  - Guix can bootstrap its entire C compiler toolchain starting from a tiny 357-byte binary seed (`stage0`), completely eliminating compiler backdoors (Ken Thompson's "Trusting Trust" attack)!

### The Imperfect World: Consumer Hardware & The Driver Dilemma

GNU Guix is maintained by the GNU Project, which means its default configuration adheres strictly to the **GNU Free System Distribution Guidelines (FSDG)**:

  - The default kernel is **Linux-Libre** (the Linux kernel stripped of all non-free binary firmware blobs).
  - No proprietary graphics drivers (like NVIDIA's proprietary driver) or proprietary commercial apps are included in official channels.

#### The Reality of Modern Laptops

While this ethical purity is noble, modern consumer hardware is often hostile to free software:

  - **Wi-Fi & Bluetooth**: Almost all modern Intel (AX200/AX211), Realtek (RTL8821), and Broadcom wireless chips require proprietary firmware blobs loaded onto the chip at boot time. Without these blobs, the operating system cannot even see the Wi-Fi card.
  - **Graphics**: NVIDIA GeForce and RTX discrete GPUs require proprietary firmware and kernel modules for hardware 3D acceleration, CUDA compute, and external display output.
  - **CPU Microcode**: Modern Intel and AMD x86 processors contain microcode vulnerabilities (Spectre, Meltdown, Retbleed, Downfall, Zenbleed). Mitigating these requires loading proprietary CPU microcode updates at early boot.
  - **Workplace Software**: Corporate communication tools like Slack, Zoom, Microsoft Teams, and Google Chrome are closed-source.

If you attempt to install pure Guix System on a modern gaming laptop or ultrabook without proprietary firmware, you may find yourself with no Wi-Fi, no GPU acceleration, and an unaccelerated software display renderer.

### Nonguix: The Pragmatic Bridge

To solve this dilemma without compromising the core project's principles, the community created **Nonguix** (<https://gitlab.com/nonguix/nonguix>).

Nonguix is an independent, decentralized channel that packages:

  - **Vanilla Linux Kernel (`linux`)**: The full upstream Linux kernel containing all driver blobs.
  - **`linux-firmware`**: Binary firmware packages for Intel, AMD, Realtek, MediaTek, and Broadcom.
  - **`microcode-initrd`**: Early-boot CPU microcode loader for Intel and AMD processors.
  - **Proprietary Software**: Steam, Spotify, Google Chrome, Discord, Slack, and NVIDIA drivers.
  - **Pre-Built Binary Substitutes**: A dedicated build farm at `https://substitutes.nonguix.org` so you never have to wait hours compiling the Linux kernel or Chromium on your laptop!

> [!WARNING]
> **⚠️ Caution: Footgun Detected!: Compiling the Linux Kernel by Mistake**
>
> If you use Nonguix without authorizing its pre-built substitute server, Guix will happily download the 150MB Linux kernel source tarball and compile it on your machine, spinning your laptop fans at 100% for 45 minutes! Always authorize `substitutes.nonguix.org` before running system reconfiguration.

<div align="center">
  <img src="images/nonguix_laptop.jpg" width="720" alt="Figure 13.1: The GNU Gnu wizard high-fiving a modern laptop: Flawless Wi-Fi, crisp audio, and GPU acceleration through Nonguix without sacrificing declarative purity."/>
  <br/>
  <em>Figure 13.1: The GNU Gnu wizard high-fiving a modern laptop: Flawless Wi-Fi, crisp audio, and GPU acceleration through Nonguix without sacrificing declarative purity.</em>
</div>

### Case Study: The Ultimate Real-World Workstation / Laptop

Let us bring everything together with a complete, production-ready `/etc/config.scm` for a modern laptop or desktop with Wi-Fi, CPU microcode updates, sound (PipeWire), and power management:
```scheme
;; /etc/config.scm - Battle-tested real-world laptop configuration
(use-modules (gnu)
             (gnu system nss)
             ;; Nonguix modules for kernel and firmware
             (nongnu packages linux)
             (nongnu system linux-initrd))

(use-service-modules desktop networking ssh cups sound)
(use-package-modules certs fonts gnome linux package-management version-control)

(operating-system
  (host-name "nomad-thinkpad")
  (timezone "America/New_York")
  (locale "en_US.utf8")

  ;; 1. Use the non-libre Linux kernel with early CPU microcode updates
  (kernel linux)
  (initrd microcode-initrd)
  (firmware (list linux-firmware))

  ;; 2. Bootloader Configuration (UEFI GRUB)
  (bootloader (bootloader-configuration
                (bootloader grub-efi-bootloader)
                (targets '("/boot/efi"))
                (keyboard-layout keyboard-layout)))

  ;; 3. Storage and Filesystems
  (file-systems (cons* (file-system
                         (mount-point "/")
                         (device (file-system-label "guix-root"))
                         (type "ext4"))
                       (file-system
                         (mount-point "/boot/efi")
                         (device (uuid "ABCD-1234" 'fat))
                         (type "vfat"))
                       %base-file-systems))

  ;; 4. User Configuration
  (users (cons (user-account
                 (name "sudheer")
                 (group "users")
                 (supplementary-groups '("wheel" "netdev" "audio" "video" "kvm" "lp"))
                 (home-directory "/home/sudheer"))
               %base-user-accounts))

  ;; 5. System-wide Packages
  (packages (append (list nss-certs
                          font-dejavu
                          font-google-noto
                          git
                          emacs)
                    %base-packages))

  ;; 6. System Services & Nonguix Substitute Server
  (services
    (append
      (list (service gnome-desktop-service-type)
            (service bluetooth-service-type
              (bluetooth-configuration
                (auto-enable? #t))))

      ;; Modify default services to add Nonguix pre-built binary caches
      (modify-services %desktop-services
        (guix-service-type config =>
          (guix-configuration
            (inherit config)
            (substitute-urls
              (append (list "https://substitutes.nonguix.org"
                            "https://bordeaux.guix.gnu.org")
                      %default-substitute-urls))
            (authorized-keys
              (append (list (plain-file "nonguix-signing-key"
                              "(public-key
 (ecc
  (curve Ed25519)
  (q #C1FD53E5D4A3D2A0B388D378307D5E06294D2AC7F453EB278F36990C28A13D02#)))"))
                      %default-authorized-guix-keys))))))))
```

### The Best of Both Worlds

With this architecture, you achieve what was once thought impossible in the Linux world:

  - **100% Real-World Hardware Compatibility**: Flawless Wi-Fi, Bluetooth audio, sleep/suspend, and GPU acceleration.
  - **100% Declarative Purity**: Your entire operating system is defined in one version-controlled Scheme file.
  - **Zero Fear of Breakage**: Every update generates a new bootloader entry. If an experimental kernel update misbehaves, selecting Generation $N-1$ in GRUB returns your machine to working order in 10 seconds.

Whether deploying computational clusters across hundreds of supercomputer nodes or running a sleek laptop workstation, GNU Guix provides the ultimate foundation for reliable computing.

[⬆ Back to Table of Contents](#-table-of-contents)



## Chapter 14: The Alchemist's Workbench: Practical Debugging, REPL Mastery, and Emacs Workflows

> *""If you cannot inspect the living tissue of your operating system while it breathes, you are not administering a computer; you are merely performing archaeology on its corpses.""*
> 
> — **The Lisp Sysadmin**

Up to this point in our journey, we have celebrated the declarative serenity of GNU Guix. We have declared operating systems in single files, constructed hermetic development shells, traveled through time with channel pins, and packaged software with functional purity.

And yet, every developer eventually encounters that fateful afternoon: you add a new service to your `/etc/config.scm`, or write a custom package definition for an internal library, and type:
```bash
sudo guix system reconfigure /etc/config.scm
```

Instead of instantaneous enlightenment, your terminal erupts into a 40-line cascade of Guile Scheme stack traces:
```bash
Backtrace:
In ice-9/boot-9.scm:
  1752:10 18 (with-exception-handler _ _ #:unwind? _ # _)
In gnu/services.scm:
   884:32 17 (loop _ #f)
In ice-9/boot-9.scm:
  1685:16 16 (raise-exception _ #:continuable? _)
  1685:16 15 (raise-exception _ #:continuable? _)
ice-9/boot-9.scm:1685:16: In procedure struct-vtable: Wrong type argument: #f
```

> [!CAUTION]
> **😭 Tears of the Imperative Developer: The Imperative Developer in the Land of Parentheses**
>
> If you come from an imperative background, your standard debugging instincts immediately trigger:
> 
>   - In Python or Node.js, you would scatter `print("HERE 1")` and `console.log()` statements across the codebase.
>   - In Docker, you would run `docker run -it broken-image /bin/bash` to poke around the filesystem interactively.
>   - In Ubuntu or Arch, you would run `strace -f`, inspect `/var/log/syslog`, or rebuild packages with manual `./configure && make` invocations.
> 
> In Guix, none of these habits seem to work at first glance! The build runs inside an isolated chroot container that vanishes when a failure occurs. The configuration is evaluated by a Scheme daemon, not executed as a Bash script. And that terrifying backtrace references `ice-9/boot-9.scm`—a core Guile internal file you didn't write and certainly don't want to debug on a Friday afternoon!

Here is the liberating truth: **GNU Guix is not a static tool parsing dead configuration files. It is an interactive, introspectable Lisp environment.** 

Because Guix is built on GNU Guile Scheme, you have access to interactive REPLs, structural record reflection, step-by-step debuggers, instant source navigation, and live system inspection that leave traditional Unix distributions decades behind. 

In this chapter, we transform you from a confused observer deciphering cryptic backtraces into a **Diagnostic Alchemist** equipped with the complete Guix debugging workbench.

### The Three Diagnostic Domains: Where Did It Fail?

The first rule of Guix debugging is identifying **which stage** of the evaluation lifecycle failed. Errors in Guix fall into three distinct domains:

  - **Evaluation Time (Scheme Evaluation)**:
    
      - *When*: Happens while Guix is reading and evaluating your Scheme code (`config.scm`, `manifest.scm`, or package recipe) to compute the dependency graph.
      - *Symptoms*: Guile backtraces, syntax errors, unbound variables, wrong record types, or cycle errors in the service extension graph.
      - *Tooling*: `guix repl`, Guile metacommands, Geiser, and record accessors.
    

  - **Build Time (Derivation Execution inside Daemon Sandbox)**:
    
      - *When*: Scheme evaluation succeeded and produced a derivation (`.drv`), but compiling or installing the software inside the isolated `/tmp/guix-build-...` container failed.
      - *Symptoms*: Compiler errors (`gcc: error: ld returned 1 exit status`), failed unit tests, missing patch targets, or network errors during tests.
      - *Tooling*: `guix build -K` (`–keep-failed`), `–log-file`, and interactive chroot reproduction via `guix shell -D`.
    

  - **Runtime (Shepherd Init and Daemons)**:
    
      - *When*: The system built and reconfigured successfully, but a system service (e.g. Nginx, PostgreSQL, OpenSSH) crashes or refuses to start at boot.
      - *Symptoms*: `herd status` shows a service in `stopped` state, or network daemons fail to bind ports.
      - *Tooling*: `herd detailed-status`, `herd doc`, `/var/log/shepherd.log`, and ephemeral virtual machines (`guix system vm`).
    

### CLI Triage: Crime Scene Investigation in the Store

When a build fails, the `guix-daemon` strictly adheres to the principle of cleanliness: it deletes the temporary build sandbox to prevent disk clutter. This is wonderful for disk hygiene, but infuriating when you need to know why `make check` threw a core dump.

#### Saving the Crime Scene: `guix build -K`

The single most valuable command-line flag for package authors and maintainers is `-K` (or `–keep-failed`):
```bash
# Keep the build directory intact upon error
guix build -K my-broken-package
```

When the build fails, Guix prints the exact path of the preserved build directory:
```bash
builder for `/gnu/store/...-my-broken-package-1.0.drv' failed with exit code 1
note: keeping build directory `/tmp/guix-build-my-broken-package-1.0.drv-0'
```

> [!TIP]
> **💡 Guix Wizard Pro-Tip: Anatomy of a Preserved Build Chroot**
>
> Inside `/tmp/guix-build-<name>.drv-0`, you will find the exact state of the universe at the moment of failure:
> 
>   - `environment-variables`: A flat shell script containing every single environment variable (`PATH`, `CPATH`, `LIBRARY_PATH`, `PKG_CONFIG_PATH`) set by the build system.
>   - The extracted upstream source code, intermediate object files (`.o`), and build artifacts.
>   - `config.log` or `CMakeError.log`: Detailed compiler probes showing why configure scripts failed.
>   - `test-suite.log`: The complete stdout/stderr of failed unit test suites.
> 

#### Re-entering the Build Environment Interactively

Don't just inspect the files—re-enter the build environment and run the commands yourself! Using `guix shell` with the `-D` (development environment) flag, you can spawn an interactive shell with every dependency present, source the environment variables, and run a debugger:
```bash
# 1. Step into an interactive shell with all build inputs exposed
guix shell -D my-broken-package -- bash

# 2. Navigate to the preserved build directory
cd /tmp/guix-build-my-broken-package-1.0.drv-0/source

# 3. Source the exact build environment captured by the daemon
source ../environment-variables

# 4. Run the failing step directly with gdb or verbose flags
make test
# or
gdb --args ./tests/failing-test-binary
```

You have now bridged the gap between pure functional containers and the raw interactive power of GNU/Linux. Once you fix the bug, exit the shell and delete the directory in `/tmp`.

#### Inspecting Build Logs: `guix build –log-file`

Never squint at a fast-scrolling terminal to catch a compiler warning. Every build log is compressed and preserved in `/var/log/guix/drvs/`:
```bash
# View the build log of any package by name
guix build --log-file nginx | less

# Or view the log of a specific derivation path
guix build --log-file /gnu/store/5q3...-nginx-1.24.0.drv | grep -i error
```

If a build was downloaded as a pre-built binary substitute from a continuous integration server (such as `ci.guix.gnu.org`), Guix will fetch the remote build log over the network automatically!

#### Forensic Dependency Graphing: `guix graph` and `guix size`

Have you ever wondered: *"Why is my tiny 2\,MB CLI tool pulling in 1.4\,GB of dependencies including Qt5 and Python?"*

Before tearing your hair out, use `guix size` and `guix graph` to locate the culprit:
```bash
# Inspect the closure size breakdown of a package
guix size my-tool
```

Guix prints a beautiful table showing every package in the closure, its self-size, its total dependency closure, and the percentage of the overall disk space it occupies:
```bash
store item                               total-size (MiB)  self-size (MiB)
/gnu/store/...-gcc-11.3.0-lib                 74.2              74.2   45.2%
/gnu/store/...-glibc-2.35                     40.1              40.1   24.4%
/gnu/store/...-my-tool-1.0                    164.1              2.1    1.3%
```

To find the exact link connecting your package to an unwanted dependency:
```bash
# Output an SVG dependency graph showing the shortest path to an input
guix graph --path my-tool unwanted-dependency | dot -Tsvg > path.svg
```

You will immediately discover whether the dependency was introduced via an accidental `propagated-inputs` declaration or a hidden runtime path baked into an executable's `RUNPATH`.

### Source Navigation: Jumping Directly to Definitions

One of the greatest joys of GNU Guix is that its package recipes and system services are not hidden behind proprietary databases, obfuscated binary manifests, or disparate shell scripts. They are readable Scheme files sitting directly on your filesystem.

#### The Instant CLI Miracle: `guix edit`

Want to see how the official Guix maintainers packaged `postgresql`, `emacs`, or `linux-libre`? You don't need to open a web browser or search GitHub:
```bash
guix edit postgresql
```

`guix edit` queries Guile's internal source properties, resolves the file and line number where `postgresql` was defined via `define-public`, and immediately opens your configured `$EDITOR` (or `$VISUAL`) at that exact line!
```bash
# Jump to the definition of a package in your favorite editor
EDITOR="emacsclient -c" guix edit nginx
# or
EDITOR="nvim" guix edit rust
```

#### Locating Services and System Modules

While `guix edit` works for package recipes, Guix System services live inside the `gnu/services/` module tree. You can find the exact filesystem location of any Guix module using Scheme's `search-path` inside a one-line evaluation:
```bash
# Find the exact path of the desktop services module
guix repl -e '(display (search-path %load-path "gnu/services/desktop.scm"))'
```

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: The Guix Source Code is the Ultimate Manual**
>
> The official Guix documentation is extensive, but the source code itself is often even clearer:
> 
>   - Package definitions live in `gnu/packages/<category>.scm` (e.g. `gnu/packages/web.scm`, `gnu/packages/python.scm`).
>   - System services live in `gnu/services/<category>.scm` (e.g. `gnu/services/ssh.scm`, `gnu/services/networking.scm`).
>   - Service configuration records are defined using `define-configuration`. Looking at the source file shows you every configurable field, its default value, and its accepted types in 10 seconds flat!
> 

### The REPL-Driven Workflow: Interrogating the Living System

In traditional systems, testing whether your configuration is syntactically and structurally valid requires running the full reconfigure command and hoping for the best. 

In Guix, you have `guix repl`.

Unlike running vanilla `guile`, `guix repl` initializes Guile with the complete Guix module tree, your configured channels, and the store connection automatically loaded into the environment.

#### Dissecting an `operating-system` Definition Live

Let us open `guix repl` and inspect our system configuration:
```bash
$ guix repl
GNU Guile 3.0.9
Copyright (C) 1995-2023 Free Software Foundation, Inc.
guile>
```

Load the necessary modules and parse your system definition file:
```scheme
;; 1. Load system, service, and package modules
(use-modules (gnu)
             (gnu system)
             (gnu services)
             (ice-9 pretty-print))

;; 2. Evaluate and instantiate your configuration file
(define os (primitive-load "/etc/config.scm"))
```

The variable `os` now holds a live `<operating-system>` Scheme record object! You can now query any aspect of your machine using standard record accessors:
```scheme
;; What host name is declared?
(operating-system-host-name os)
;; => "antigravity-workstation"

;; What timezone?
(operating-system-timezone os)
;; => "America/New_York"

;; List all packages declared directly in the operating-system record
(map package-name (operating-system-packages os))
;; => ("vim" "git" "htop" "tmux" "curl")
```

#### Filtering and Querying Services

The most complex part of any Guix System configuration is the service graph. In the REPL, you can inspect and query every single service running on the system:
```scheme
;; Extract all services
(define svcs (operating-system-services os))

;; How many services are configured (including default base services)?
(length svcs)
;; => 47

;; Find the OpenSSH service
(use-modules (gnu services ssh))

(define ssh-matches
  (filter (lambda (s) (eq? (service-kind s) openssh-service-type))
          svcs))

(define ssh-svc (car ssh-matches))
```

Now inspect the value (the configuration record) passed to that service:
```scheme
(define ssh-cfg (service-value ssh-svc))

;; Inspect individual fields
(openssh-configuration-port-number ssh-cfg)
;; => 22

(openssh-configuration-permit-root-login ssh-cfg)
;; => #f
```

> [!TIP]
> **💡 Guix Wizard Pro-Tip: Testing `modify-services` in the REPL**
>
> Are you trying to write a complex `modify-services` clause to customize GDM, UDev rules, or OpenSSH, but keep getting syntax errors?
>
> Don't test it by running `guix system reconfigure`! Paste your `modify-services` expression directly into `guix repl` and evaluate it against `svcs`. If it produces a modified list of services without throwing an exception, you know your syntax and field types are 100% correct.

#### Inspecting Package Recipes and Inputs

You can also use the REPL to inspect package objects, check for security updates, and evaluate dependencies:
```scheme
(use-modules (gnu packages web))

;; Look up a package by specification
(define nginx (specification->package "nginx"))

;; Check package version and license
(package-version nginx)
;; => "1.24.0"

(package-license nginx)
;; => #<license: bsd-2>

;; Inspect its direct inputs
(map car (package-inputs nginx))
;; => ("openssl" "pcre" "zlib")

;; Inspect build arguments passed to the build system
(package-arguments nginx)
;; => (#:tests? #f #:configure-flags '("--with-http_ssl_module" ...))
```

#### Testing G-Expressions Without Building the Universe

In [Chapter 10](#chapter-10-build-phases-g-expressions-and-shebangs), we learned that G-Expressions (`#\~{}`) represent code staged for execution inside store derivations. How do you test what a G-expression expands to without running a 30-minute system build?

You can **lower** any object to a store derivation right inside the REPL:
```scheme
(use-modules (guix gexp)
             (guix store)
             (guix derivations))

;; Open a live connection to the guix-daemon
(define store (open-connection))

;; Lower a package reference to its store derivation
(run-with-store store
  (lower-object (specification->package "hello")))
;; => #<derivation /gnu/store/...-hello-2.12.1.drv => ...>
```

#### Guile REPL Metacommands: Your Interactive Swiss Army Knife

Guile's REPL provides built-in metacommands (prefixed with a comma `,`) that turn the terminal into an interactive debugger:

| **Metacommand** | **Function and Usage** |
| :--- | :--- |
| `,describe <expr>` | View docstring, parameter list, and module location of any procedure or macro. |
| `,inspect <expr>` | Launch an interactive tree browser for any record, hash-table, vector, or closure. |
| `,trace (<call>)` | Trace procedure execution, showing arguments and return values at each stack frame. |
| `,step (<call>)` | Step interactively through expression evaluation frame-by-frame. |
| `,bt` (backtrace) | In an error break loop, print the complete call stack with local variables. |
| `,locals` | In a debugger break frame, display all bound local variables. |
| `,quit` | Exit the REPL session. |

*Essential GNU Guile REPL metacommands.*

For example, typing `,inspect ssh-cfg` launches an interactive curses-style inspector where you can arrow through every field of the OpenSSH configuration record in real time!

### The Lisp Nirvana: Emacs and Geiser Integration

If `guix repl` gives you terminal-based superpowers, pairing GNU Guix with **GNU Emacs** and **Geiser** elevates your workflow to absolute nirvana.

In conventional editors (VS Code, Sublime, Vim), Scheme code is treated as static text with syntax highlighting. In Emacs with Geiser, your editor buffer is connected directly to a living Scheme evaluation process.

> [!TIP]
> **💡 Guix Wizard Pro-Tip: The Lisp Alchemist's Cockpit**
>
> In an Emacs-Geiser workflow, your screen is typically split into two interactive halves:
> 
>   - **Left Window (Source Buffer)**: Your `config.scm` or package definition file. You write expressions, jump to definitions with `M-.`, and send definitions to the compiler.
>   - **Right Window (Guile REPL Buffer)**: The live Guix runtime. It evaluates your expressions, prints record representations, and lets you interrogate values interactively.
> 

#### Setting Up the Environment in 60 Seconds

You do not need to spend days configuring an elaborate Emacs setup. You can launch a complete, hermetic Emacs development environment with all required Guix extensions in a single command using `guix shell`:
```bash
guix shell emacs \
           emacs-geiser \
           emacs-geiser-guile \
           emacs-guix \
           emacs-paredit \
           -- emacs
```

#### The Geiser Workflow: Interactive Evaluation

Open your `config.scm` or custom package file in Emacs, then start Geiser:

`M-x geiser-guile`

This splits your window and launches a dedicated Guile REPL connected directly to your buffer.

Here are the four essential keybindings that will change the way you write Guix configurations forever:

  - **Evaluate S-Expression Preceding Cursor (`C-x C-e`)**:
    Place your cursor immediately after any closing parenthesis and press `C-x C-e`. Geiser evaluates that specific expression in the REPL and displays the result in the echo area.
  
  - **Evaluate Entire Top-Level Definition (`C-c C-c`)**:
    Place your cursor anywhere inside a `(define-public ...)` package or a `(define os ...)` block and press `C-c C-c`. The definition is compiled and sent to the running Guix session instantly.

  - **Switch Between Buffer and REPL (`C-c C-z`)**:
    Toggle instantaneously between your Scheme source buffer and the interactive REPL prompt.

  - **Instant Documentation Lookup (`C-c C-d C-d`)**:
    Place your cursor on any Guix procedure or macro (e.g. `modify-phases`, `service-extension`) and press `C-c C-d C-d` to display its complete documentation in a dedicated buffer.

#### The Holy Grail: Jump to Definition with `M-.`

This is the single feature that transforms Guix from an overwhelming wall of Scheme code into an intuitive, self-documenting playground:

Place your cursor on **any** symbol in your buffer:

  - An unfamiliar service type: `dhcp-client-service-type`
  - A configuration record: `tor-configuration`
  - A build system helper: `substitute*`
  - A package definition: `git`

Press:

**`M-.`** \normalsize\quad (`geiser-edit-symbol-at-point`)

Emacs will **instantly jump to the exact source file and line number in the GNU Guix codebase** where that symbol was defined! 

You can read how the service is constructed, see what default arguments it expects, inspect its Shepherd action scripts, and copy patterns directly from the core maintainers.

When you are finished reading, press:

**`M-,`** \normalsize\quad (`geiser-pop-symbol-stack`)

and Emacs jumps right back to your personal configuration file. You will never need to hunt through external wiki pages or outdated blog posts again.

#### Browsing Guix Visually with `guix.el`

The `emacs-guix` package provides a rich visual interface to Guix package management directly inside Emacs buffers:

  - `M-x guix-packages-by-name`: Search for packages with an interactive tabular browser showing descriptions, homepages, licenses, and outputs.
  - `M-x guix-generations`: View your system and profile generation history. You can compare and diff any two generations with a single keystroke (`d`) to see exactly which packages were added, removed, or upgraded!
  - `M-x guix-system-generations`: Inspect, activate, or delete Guix System generations visually.

### Runtime Triage: Shepherd Services and Disposable Virtual Machines

What happens when your package builds, your `config.scm` evaluates cleanly, `guix system reconfigure` succeeds, but your computer reboots and the web server or desktop manager fails to start?

#### Diagnosing Shepherd Service Failures

GNU Shepherd ([Chapter 7](#chapter-7-gnu-shepherd-the-lisp-powered-init-system)) is your PID 1 supervisor. When a service fails to launch, query it with `herd`:
```bash
# Check status of all running and stopped services
herd status

# Get deep diagnostics on a failing service
herd detailed-status nginx
```

`herd detailed-status` displays:

  - Whether the service is currently running or stopped.
  - The PID of the running daemon.
  - Recent exit statuses and timestamps (e.g. `exited with code 1 at 14:02:11`).
  - The **Respawn count**: whether Shepherd tried to restart the service and gave up because it was crashing in an infinite loop.

#### Inspecting Shepherd and System Logs

Shepherd records all service stdout, stderr, and lifecycle transitions in `/var/log/`:
```bash
# View Shepherd daemon events
sudo less /var/log/shepherd.log

# View system messages and kernel syslog
sudo less /var/log/messages

# Follow logs in real time while starting a service
sudo tail -f /var/log/shepherd.log
```

#### Zero-Risk Testing with Ephemeral Virtual Machines

Never test a radical system reconfiguration (such as modifying your display manager, core PAM authentication rules, or disk encryption) directly on bare metal if you cannot afford downtime.

Guix System has a miraculous built-in superpower: `guix system vm`.
```bash
# Compile your configuration into a self-contained QEMU virtual machine script
guix system vm /etc/config.scm
```

This command evaluates your configuration, builds any missing packages, and produces a single executable script in `/gnu/store/...-run-vm.sh`:
```bash
# Launch your proposed operating system in a window!
$(guix system vm /etc/config.scm) -m 2048 -smp 2 -net nic -net user,hostfwd=tcp::2222-:22
```

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: The Power of the Ephemeral VM**
>
> When you boot this virtual machine:
> 
>   - It boots your **exact** declared kernel, Shepherd services, user accounts, and desktop environment inside QEMU.
>   - It shares the immutable host store (`/gnu/store`) read-only via 9p virtio filesystem sharing, so starting the VM takes less than 5 seconds!
>   - Any disk writes in the VM are redirected to an ephemeral QEMU overlay file. Your host machine is 100% protected.
>   - You can SSH into your VM on port 2222 (`ssh -p 2222 user@localhost`) to test daemons, verify network configurations, and validate Shepherd scripts before running `guix system reconfigure` on bare metal.
> 

### Real-World Case Studies: Finding Your Way in the Fog

Abstract theory is comforting, but true diagnostic wisdom is forged in the fires of actual failure. Here are six battle-tested case studies representing the most frequent stumbling blocks encountered by newcomers, along with the exact step-by-step investigative workflows to resolve them.

#### Case Study 1: The Missing Module and the Unbound Variable Mystery

**The Setup**: You are configuring a developer workstation. You decide to add the Bluetooth service and a Tor daemon to your `services` list in `/etc/config.scm`:
```scheme
(operating-system
  ;; ...
  (services
    (cons* (service bluetooth-service-type)
           (service tor-service-type)
           %desktop-services)))
```

**The Error**: You run `sudo guix system reconfigure /etc/config.scm` and get slapped with:
```bash
/etc/config.scm:42:19: error: bluetooth-service-type: unbound variable
hint: Did you forget `(use-modules (gnu services desktop))'?
```

You dutifully add `(use-modules (gnu services desktop))` at the top of the file and re-run. Now Guix complains:
```bash
/etc/config.scm:43:19: error: tor-service-type: unbound variable
```

Notice that for `tor-service-type`, **Guix offers no hint at all!**

**The Investigation**: Where on earth is `tor-service-type` defined? Do you comb through 1,200 source files in Guix?
No! You have three immediate tools:

  - **The Geiser Apropos Search (in Emacs)**:
    Press `C-c C-d C-a` (`geiser-apropos`) and type `tor-service`. Within half a second, Emacs scans all loaded and discovered modules and displays:
```scheme
tor-service-type: <service-type> in (gnu services networking)
```

  - **The Fast Terminal `grep` over Guix Sources**:
    If you are in a terminal, query the Scheme load path for services:
```bash
# Locate the services directory inside the store
    guix repl -e '(display (search-path %load-path "gnu/services.scm"))'
```

    Or simply grep the installed module tree:
```bash
find $(guix repl -e '(display (dirname (search-path %load-path "gnu/services.scm")))') \
      -name "*.scm" | xargs grep -l "define-public tor-service-type"
```

    It reports: `gnu/services/networking.scm`!

**The Resolution**: Add `(gnu services networking)` to your `use-modules` declaration:
```scheme
(use-modules (gnu)
             (gnu services desktop)     ; for bluetooth-service-type
             (gnu services networking))  ; for tor-service-type
```

#### Case Study 2: Record Archeology—Taming Cryptic Field Errors

**The Setup**: You want to run the OpenSSH daemon on a custom port and disable password authentication. You write:
```scheme
(service openssh-service-type
  (openssh-configuration
    (port 2222)
    (password-authentication? "no")))
```

**The Error**: You reconfigure, and Guix crashes with:
```bash
ice-9/boot-9.scm:1685:16: In procedure struct-vtable: Wrong type argument: #f
error: invalid field specifier `port`
```

Or, if you fix the field name to something plausible, you get:
```bash
error: value "no" does not match predicate boolean?
```

**The Investigation**: What are the exact field names and types for `openssh-configuration`?
Instead of guessing or reading third-party blog posts from 2019, inspect the record definition directly:

  - **In Emacs**: Put cursor on `openssh-configuration` and press `M-.`. You land directly on line 140 of `gnu/services/ssh.scm`.
  - **In Terminal**: Launch `guix repl` and inspect the record type:
```scheme
(use-modules (gnu services ssh))
    ,describe openssh-configuration
```

    Even better, instantiate the default configuration and inspect it:
```scheme
,inspect (openssh-configuration)
```

    Guile opens an interactive record browser displaying every field, its name, and its default value:
```bash
[0] port-number: 22
    [1] permit-root-login: #f
    [2] password-authentication?: #t
    [3] public-key-authentication?: #t
    [4] x11-forwarding?: #f
```

**The Revelation**:

  - The field is not `port`; it is `port-number`, expecting an exact integer.
  - The field is `password-authentication?`, expecting a Scheme boolean (`#t` or `#f`), not a string like `"no"`.

**The Resolution**:
```scheme
(service openssh-service-type
  (openssh-configuration
    (port-number 2222)
    (password-authentication? #f)))
```

#### Case Study 3: The Service Collision: "Service X provided more than once"

**The Setup**: You just bought a graphic drawing tablet or hardware security key (e.g. YubiKey). To make it work, you must add custom UDev rules. You look up `udev-service-type` and write:
```scheme
(operating-system
  ;; ...
  (services
    (cons* (service udev-service-type
             (udev-configuration
               (rules (list my-custom-udev-rules))))
           %desktop-services)))
```

**The Error**:
```bash
guix system: error: service 'udev' provided more than once
```

> [!CAUTION]
> **😭 Tears of the Imperative Developer: The Mental Model Collision**
>
> Why did this happen? In imperative distros, you just drop a file into `/etc/udev/rules.d/`. In Guix, `%desktop-services` already instantiates and configures a system-wide UDev daemon. 
>
> When you declared `(service udev-service-type ...)`, you told Guix to launch a **second, competing UDev daemon** managing the same hardware! Guix's service graph validator detects this collision and aborts before you render your system unbootable.

**The Investigation in the REPL**: Let us verify where the existing UDev service lives:
```scheme
(use-modules (gnu) (gnu services) (gnu services base))
(define svcs %desktop-services)

;; Find all services that are of kind udev-service-type
(filter (lambda (s) (eq? (service-kind s) udev-service-type)) svcs)
;; => (#<service udev 7f3b890a2c00>)
```

Indeed, UDev is already a core member of `%desktop-services`!

**The Resolution**: In Guix, you do not add a duplicate service; you **extend** the existing one. Guix provides a dedicated helper for this exact scenario:
```scheme
(use-modules (gnu services base))

(operating-system
  ;; ...
  (services
    (cons* (udev-rules-service 'my-drawing-tablet my-custom-udev-rules)
           %desktop-services)))
```

The `udev-rules-service` helper emits a service extension that automatically injects your rules into the existing UDev daemon without collision!

#### Case Study 4: The Build Crime Scene: Missing Headers and the Phantom `pkg-config`

**The Setup**: You are packaging a C utility called `fast-calc` that depends on SQLite. You write your package definition:
```scheme
(define-public fast-calc
  (package
    (name "fast-calc")
    (version "1.0")
    (source (origin ...))
    (build-system gnu-build-system)
    (inputs (list sqlite))
    (synopsis "Ultra fast calculator")
    ...))
```

**The Error**: You run `guix build -f fast-calc.scm` and get:
```bash
starting phase `configure'
checking for gcc... gcc
checking for sqlite3... no
configure: error: Package requirements (sqlite3 >= 3.0) were not met:
No package 'sqlite3' found
Consider adjusting the PKG_CONFIG_PATH environment variable...
error: in phase 'configure': returned #f
```

**The Panic**: You scream: *"I literally put `sqlite` in `inputs`! Why does configure say sqlite3 is not found?!"*

**The Forensic Investigation**:
Run the build with `-K` to capture the sandbox:
```bash
guix build -K -f fast-calc.scm
```

Guix keeps the directory in `/tmp/guix-build-fast-calc-1.0.drv-0`.
Now, step inside the exact environment:
```bash
guix shell -D -f fast-calc.scm -- bash
cd /tmp/guix-build-fast-calc-1.0.drv-0
source ./environment-variables
```

Now interrogate the environment:
```bash
# 1. Does SQLite exist in the store?
echo $CPATH
# => /gnu/store/...-sqlite-3.40.1/include

# 2. Does the .pc file exist in PKG_CONFIG_PATH?
echo $PKG_CONFIG_PATH
# => /gnu/store/...-sqlite-3.40.1/lib/pkgconfig

# 3. Can pkg-config find it?
pkg-config --modversion sqlite3
# => bash: pkg-config: command not found!
```

**The Eureka Moment**: SQLite was present, its headers were present, and its `.pc` file was in `PKG_CONFIG_PATH`. But the `configure` script used the `pkg.m4` macro to look for SQLite, and **`pkg-config` itself was never installed in the build container!**

Because `pkg-config` is a build tool executed on the build host (not a library linked into the target binary), it belongs in `native-inputs`.

**The Resolution**:
```scheme
(define-public fast-calc
  (package
    (name "fast-calc")
    ;; ...
    (native-inputs (list pkg-config))  ; <--- The missing link!
    (inputs (list sqlite))
    ;; ...))
```

Re-running `guix build -f fast-calc.scm` now succeeds in 4 seconds flat.

#### Case Study 5: Post-Reconfigure Triage: The Crashing Shepherd Daemon

**The Setup**: You configured an Nginx web server on your Guix machine to host an internal dashboard:
```scheme
(service nginx-service-type
  (nginx-configuration
    (server-blocks
      (list (nginx-server-configuration
              (listen '("80"))
              (server-name '("localhost"))
              (root "/srv/http"))))))
```

**The Symptom**: `sudo guix system reconfigure /etc/config.scm` completes cleanly. No build errors, no Scheme errors. But when you run `curl http://localhost`, you receive:
```bash
curl: (7) Failed to connect to localhost port 80: Connection refused
```

**The Investigation**:
Check Shepherd service status:
```bash
sudo herd status nginx
```

Shepherd reports:
```bash
Status of nginx:
  It is stopped.
  It is enabled.
  Provides: (nginx httpd)
  Requires: (user-processes loopback)
```

Try starting it manually:
```bash
sudo herd start nginx
```

Shepherd prints:
```bash
herd: error: Service nginx could not be started.
```

Why? Ask Shepherd for detailed forensic telemetry:
```bash
sudo herd detailed-status nginx
```

Output:
```bash
Last exit code: 1
  Respawn limit hit: 5 crashes in 3 seconds. Disabled respawning.
```

Now check the Shepherd daemon log and Nginx error log:
```bash
sudo tail -n 25 /var/log/shepherd.log
sudo cat /var/log/nginx/error.log
```

The error log reveals the truth in plain English:
```bash
2026/11/14 10:15:22 [emerg] 1421#1421: bind() to 0.0.0.0:80 failed (98: Address already in use)
```

**The Resolution**:
Run `sudo ss -tulpn | grep :80` to see who owns port 80. You find a stray Apache or lighttpd container running in the background! Terminate the rogue process and run `sudo herd start nginx`. The service starts instantly with `It is started [PID 1842]`.

#### Case Study 6: The Accidental 4-Hour Compile: Diagnosing Substitute Cache Misses

**The Setup**: You want to install a popular desktop application:
```bash
guix install inkscape
```

Instead of downloading pre-built binaries in 30 seconds, your laptop fans spin up to deafening speed. Your terminal prints:
```bash
The following derivation will be built:
  /gnu/store/...-gcc-11.3.0.drv
building /gnu/store/...-gcc-11.3.0.drv...
[  1%] Building CXX object ...
```

Your machine is compiling GCC and LLVM from source!

> [!WARNING]
> **⚠️ Caution: Footgun Detected!: The Gentoo Nightmare Scenario**
>
> Newcomers often panic here: *"I thought Guix had binary substitutes! Why is it compiling the entire C compiler toolchain on my dual-core laptop?!"*

**The Diagnostic Workflow**:
Stop the build immediately with `Ctrl-C`. Then investigate why substitutes were not found:

  - **Always Dry-Run First (`-n`)**:
    Before running any install, build, or reconfigure, pass `-n` (or `–dry-run`):
```bash
guix install inkscape -n
```

    Guix will tell you upfront:
    
      - `124.5 MB would be downloaded`: Pre-built binaries exist. Safe to proceed!
      - `The following derivations will be built`: No substitute exists. You will be compiling from source!
    

  - **Check Substitute Server Health with `guix weather`**:
```bash
guix weather inkscape
```

    This queries the build farm (`bordeaux.guix.gnu.org` or `ci.guix.gnu.org`) and reports whether binary substitutes are currently available for your architecture.

  - **Identify Substitute URL Configuration**:
    Check whether your `guix-daemon` is configured with authorized substitute keys and servers:
```bash
# Check authorized keys
    ls -l /etc/guix/acl
```

    If `/etc/guix/acl` is missing or empty, the daemon refuses to download remote substitutes for security reasons! Authorize the official build farm:
```bash
sudo guix archive --authorize < \
      $(guix repl -e '(display (search-path %load-path "gnu/packages/substitutes/bordeaux.guix.gnu.org.pub"))')
```

  - **Diagnose Channel Drift**:
    If you ran `guix pull` five minutes after a maintainer committed a change to the core toolchain, the continuous integration servers might still be compiling the binaries in the queue.
    
    Using `guix describe`, check your current commit. If you pulled too close to the bleeding edge, use `guix time-machine` to pin to a commit from 24 hours earlier where 100% of binary substitutes are cached.

### The Diagnostic Alchemist's Field Guide

When things go bump in the night, consult these diagnostic reference matrices:

#### Evaluation and Build Diagnostics

| **Symptom** | **Diagnostic Tool** | **Alchemical Cure** |
| :--- | :--- | :--- |
| Cryptic Guile backtrace mentioning `boot-9.scm` |  |  |
| `guix system build -d -v 2` \newline `guix repl` |  |  |
| Build fails during `make` or `make check` in chroot |  |  |
| `guix build -K <pkg>` \newline `guix shell -D <pkg>` |  |  |
| Missing C library during `configure` despite `inputs` |  |  |
| `guix build -K` \newline `environment-variables` |  |  |
| Unsure why package pulls in huge unwanted dependency |  |  |
| `guix size <pkg>` \newline `guix graph –path` |  |  |
| Cannot find where a package or service is defined |  |  |
| `guix edit <pkg>` \newline `M-.` in Emacs / Geiser |  |  |

*Evaluation and Build Diagnostics.*

#### Service, Runtime, and Substitute Diagnostics

| **Symptom** | **Diagnostic Tool** | **Alchemical Cure** |
| :--- | :--- | :--- |
| Syntax error in `modify-services` or system record |  |  |
| `guix repl` \newline `primitive-load` |  |  |
| "Service X provided more than once" conflict |  |  |
| `guix repl` \newline `operating-system-services` |  |  |
| System service fails to start or crashes on boot |  |  |
| `herd detailed-status <svc>` \newline `/var/log/shepherd.log` |  |  |
| Unexpected 4-hour source compilation of core toolchain |  |  |
| `guix weather` \newline `guix build -n` |  |  |
| Fear of breaking workstation on reconfigure |  |  |
| `guix system vm config.scm` |  |  |

*Service, Runtime, and Substitute Diagnostics.*

With these tools and case studies at your command, the parentheses are no longer an impenetrable barrier. They are a transparent window into the living soul of your operating system.

[⬆ Back to Table of Contents](#-table-of-contents)



## Chapter 15: The Twin Souls: GNU Emacs and the Living Lisp Machine

> *""Emacs outshines all other editing software in approximately the same way that the noonday sun does the stars. It is not just bigger and brighter; it simply makes everything else vanish.""*
> 
> — **Neal Stephenson, In the Beginning... Was the Command Line**

Throughout the history of computer science, certain technologies have shared an almost telepathic affinity. Unix and C. The Web and JavaScript. Docker and Go. 

And then there is **GNU Guix** and **GNU Emacs**.

To describe Emacs as merely a "text editor" for GNU Guix is like describing the ocean as merely a storage medium for fish. In the Guix universe, Emacs occupies a sacred, foundational status. It is the spiritual ancestor, the primary development cockpit, the graphical interface, and the philosophical twin of GNU Guix. 

Together, they represent the modern resurrection of a dream once thought lost to computing history: **The Living Lisp Machine**.

In this chapter, we explore why Guix and Emacs are inseparable, how to install and configure Emacs on Guix, why Guix is secretly the greatest Emacs package manager on Earth, how to harness `guix.el` and Geiser, and how to combine `guix shell` with `envrc` to create the ultimate development environment.

### The Philosophy of Twin Souls: Resurrecting the Lisp Machine

In the late 1970s and 1980s, computer scientists at the MIT Artificial Intelligence Laboratory and Symbolics created the **Lisp Machine**—a computer where there was no distinction between the operating system, the development environment, and the applications. Everything was Lisp. The code was malleable, self-documenting, and introspectable at runtime. You did not compile a static binary, deploy it, watch it crash, and read a core dump. You stepped directly into the living, running environment and reshaped reality on the fly.

> [!TIP]
> **💡 Guix Wizard Pro-Tip: The Architecture of the Modern Lisp Machine**
>
> When you pair GNU Guix with GNU Emacs, the computing stack becomes conceptually unified:
> 
>   - **Desktop & Windows**: EXWM (Emacs Lisp)
>   - **Editing & Workflow**: GNU Emacs buffers, Dired, Magit (Emacs Lisp)
>   - **Userland & Dotfiles**: Guix Home (Guile Scheme)
>   - **Package Management**: GNU Guix profiles and derivations (Guile Scheme)
>   - **Init System & PID 1**: GNU Shepherd (Guile Scheme)
>   - **Operating System Definition**: `/etc/config.scm` (Guile Scheme)
> 
> From system boot to the cursor in your text buffer, every layer is programmable, declarative, and inspectable in Lisp.

The Unix revolution ultimately eclipsed the Lisp Machine. Unix made pragmatic compromises: it was built in C, relied on opaque binary files, and treated the filesystem as a flat hierarchy of mutable text files. 

For forty years, GNU Emacs carried the torch of the Lisp Machine in exile. Inside Emacs, everything was Emacs Lisp (Elisp). Every buffer, every keybinding, every window, and every mode could be inspected, modified, and extended while the editor was running. But the moment Emacs interacted with the underlying host operating system, it collided with the harsh, cold reality of mutable Unix: brittle shared libraries in `/usr/lib`, broken package updates, and global environment variables.

> [!IMPORTANT]
> **✨ Functional Alchemy & Arcana: The Full Stack Lisp Reunion**
>
> GNU Guix completes the circle. Guix took the purely functional principles of Eelco Dolstra's Nix and paired them with **GNU Guile Scheme**. 
>
> When you run Guix System with Emacs:
> 
>   - Your kernel and init system (GNU Shepherd) are controlled by Guile Scheme.
>   - Your system configuration (`config.scm`) is Guile Scheme.
>   - Your user environment (Guix Home) is Guile Scheme.
>   - Your package recipes and build phases are Guile Scheme.
>   - Your editor, mail client, terminal emulator, and window manager (EXWM) are Emacs Lisp.
> 
> The boundary between "the operating system" and "the editor" completely dissolves. You are once again sitting at an introspectable, programmable, unified Lisp Machine.

### Installing Emacs on Guix: Choosing the Right Flavor

Because Emacs is a central pillar of the GNU Project, Guix provides first-class, finely tuned packages for every conceivable deployment target.

| **Package Name** | **Intended Use Case and Architecture** |
| :--- | :--- |
| `emacs-pgtk` | **The Modern Standard.** Built with Pure GTK (PGTK). Delivers native Wayland rendering without XWayland blurring or HiDPI scaling issues. Ideal for Sway, Hyprland, and GNOME Wayland. |
| `emacs` | **The Classic GUI.** Built with standard X11 and GTK3 support. Recommended for traditional X11 window managers (XFCE, i3, Openbox). |
| `emacs-no-x` | **The Headless Server.** Stripped of all graphical, image, and sound libraries. Compiles rapidly and runs directly inside a terminal over SSH. |
| `emacs-wide-int` | Built with 64-bit integer support on 32-bit hardware architectures. |

*The primary Emacs packages available in GNU Guix.*

#### Native Compilation (`native-comp`) Out of the Box

Modern Emacs features **Native Compilation** (often called `gccemacs` or `native-comp`). Instead of interpreting Elisp byte-code (`.elc`), Emacs uses `libgccjit` to compile Elisp directly into native machine code (`.eln`), yielding $2.5\times$ to $5\times$ speedups across syntax highlighting, language servers, and buffer operations.

> [!TIP]
> **💡 Guix Wizard Pro-Tip: Guix Solves the `libgccjit` ABI Nightmare**
>
> In traditional distributions (like Ubuntu, Debian, or Arch), setting up native compilation is often a fragile nightmare: you must install experimental `gcc` development packages, ensure `libgccjit` matches your running compiler version, and endure spontaneous background compilation locks that freeze the editor.
>
> In GNU Guix, **native compilation is enabled by default** in the core `emacs` and `emacs-pgtk` packages! The `guix-daemon` compiles core Elisp libraries into native `.eln` binaries ahead of time inside the hermetic store. You get blazing fast performance with zero compilation stutter on your desktop.

To install the flagship Wayland-native package into your active profile:
```bash
guix install emacs-pgtk
```

### Why Guix is the World's Best Emacs Package Manager

Ask any veteran Emacs user about package management, and their eyes will glaze over with memories of shattered configurations.

Historically, Emacs users relied on `package.el` pulling packages from **MELPA** (Milkypostman's Emacs Lisp Package Archive), or more recently on tools like `straight.el` and `elpaca` that clone Git repositories directly.

> [!CAUTION]
> **😭 Tears of the Imperative Developer: The MELPA Fragility Trap**
>
> Why do traditional Emacs package managers fail?
> 
>   - **Bleeding Edge Breakage**: MELPA builds packages automatically from the `master` branch of thousands of upstream Git repositories. You run `M-x package-upgrade-all` on a Monday morning, a maintainer pushed an untested commit twenty minutes ago, and your editor fails to boot.
>   - **The Native C Library Wall**: What happens when an Emacs package needs a compiled C library?
>     
>       - `vterm` (blazing fast terminal): Needs `libvterm` and `cmake`.
>       - `pdf-tools` (vector PDF viewer): Needs `poppler`, `cairo`, and `libpng`.
>       - `mu4e` (email client): Needs `mu` and the `xapian` search engine.
>       - `telega` (Telegram client): Needs the C++ `tdlib` daemon.
>     
>     Traditional Emacs package managers cannot install C libraries! They fail with cryptic compilation logs, forcing the user to imperatively run `sudo apt install libvterm-dev` or fiddle with build flags.
> 

GNU Guix completely eliminates this problem. In Guix, **Emacs packages are first-class citizen packages in the store**, prefixed with `emacs-`:
```bash
# Search over 1,500+ curated Emacs packages in Guix
guix search emacs-magit
guix search emacs-vterm
guix search emacs-pdf-tools
```

When you install `emacs-vterm` via Guix:

  - Guix fetches the verified source code.
  - Guix compiles the C module (`vterm-module.so`) inside a clean chroot against the exact, immutable `libvterm` in the store.
  - Guix natively compiles all Elisp files into `.eln` machine code.
  - When Emacs opens, `vterm` works instantly. Zero compilation, zero CMake errors, zero missing header warnings!

Furthermore, because your Emacs packages reside in a transactional Guix profile, upgrading your plugins is protected by **instant atomic rollbacks**:
```bash
# Upgraded your Emacs packages and don't like the new behavior?
guix package --roll-back
```

Your previous generation is restored in 20 milliseconds.

### The Mechanics: Autoloads, `EMACSLOADPATH`, and Instant Startup

How does GNU Emacs find packages installed through Guix?

When you install any `emacs-*` package in your user profile, Guix creates a dedicated site directory:

`~/.guix-profile/share/emacs/site-lisp/`

Inside this directory, Guix generates a unified autoloads file: `guix-emacs-autoloads.el`.

#### The System Crafters Instant Startup Pattern

In traditional setups, Emacs spends hundreds of milliseconds during startup initializing `package.el`, scanning `~/.emacs.d/elpa`, and checking for updates over HTTP.

As popularized by David Wilson of **System Crafters** (<https://systemcrafters.net>), when you allow GNU Guix to manage your Emacs packages, you can completely disable `package.el` at startup!

Create or edit your `~/.emacs.d/early-init.el`:
```scheme
;;; early-init.el --- The Instant Startup Hack -*- lexical-binding: t; -*-

;; 1. Prevent package.el from activating packages at startup.
;; Guix already manages our packages and sets up autoloads!
(setq package-enable-at-startup nil)

;; 2. Prevent package.el from contacting ELPA/MELPA archives
(setq package-archives nil)

;; 3. Temporarily raise the garbage collection threshold during startup
(setq gc-cons-threshold (* 100 1024 1024))

;; 4. Restore normal GC threshold after startup completes
(add-hook 'emacs-startup-hook
  (lambda ()
    (setq gc-cons-threshold (* 8 1024 1024))))
```

With this single adjustment, Emacs startup time typically plunges from 3.5 seconds down to **under 0.2 seconds**! All your packages are already natively compiled, indexed by Guix's autoloads, and ready in memory.

#### Using `use-package` with Guix

You can still use the beloved `use-package` macro to structure your configuration cleanly. Since Guix ensures all packages are already installed, you simply omit `:ensure t`:
```scheme
;;; init.el --- Clean, Reproducible Configuration

;; Vertico for minimal, vertical completion
(use-package vertico
  :init
  (vertico-mode 1))

;; Orderless for fuzzy space-separated matching
(use-package orderless
  :custom
  (completion-styles '(orderless basic)))

;; Corfu for sleek in-buffer completion popups
(use-package corfu
  :init
  (global-corfu-mode 1))

;; Magit: The greatest Git interface ever crafted
(use-package magit
  :bind ("C-x g" . magit-status))
```

### Declaring Emacs with Guix Home

In [Chapter 8](#chapter-8-guix-home-declarative-dotfiles-and-userland), we mastered declarative userlands. Let us see how to declare your entire Emacs installation, every single plugin, and your configuration file directly in Scheme using `home-emacs-service-type`.

Here is a complete, real-world snippet for your `~/.config/guix/home-configuration.scm`:
```scheme
(use-modules (gnu home)
             (gnu home services)
             (gnu home services shells)
             (gnu packages emacs)
             (gnu packages emacs-xyz)
             (gnu services))

(home-environment
  (packages
    (list
      ;; The Wayland-native editor
      emacs-pgtk

      ;; Core modern completion UI
      emacs-vertico
      emacs-orderless
      emacs-marginalia
      emacs-consult
      emacs-corfu

      ;; Development & Lisp Superpowers
      emacs-geiser
      emacs-geiser-guile
      emacs-guix
      emacs-magit
      emacs-vterm
      emacs-envrc))

  (services
    (list
      ;; Manage Emacs daemon as a Shepherd user service
      (service home-emacs-service-type
        (home-emacs-configuration
          (package emacs-pgtk)
          (server-mode? #t))) ; Starts `emacs --daemon` on login!

      ;; Symlink our version-controlled dotfiles
      (service home-files-service-type
        `((".emacs.d/early-init.el" ,(local-file "emacs/early-init.el"))
          (".emacs.d/init.el"       ,(local-file "emacs/init.el")))))))
```

When you run `guix home reconfigure`, Guix:

  - Installs `emacs-pgtk` and all specified plugins into your home profile.
  - Hermetically links your native C libraries (like `vterm`).
  - Sets up Shepherd to launch the Emacs server daemon in the background on login.
  - Deploys your `init.el` atomically.

### The Flagship Interface: `emacs-guix` (`guix.el`)

If you prefer a rich, visual buffer-based interface for managing your operating system, **Emacs-Guix** (authored by Alex Kost) turns Emacs into the ultimate Guix control center.

Install it via Guix:
```bash
guix install emacs-guix
```

Inside Emacs, type:

`M-x guix`

A magnificent dashboard appears with quick access to package searches, profile generations, system services, and store licenses.

#### Interactive Package Browsing

Run `M-x guix-packages-by-name` and type a query (for example, `firefox` or `python`). Emacs opens a tabular buffer named `*Guix Packages*`:
```bash
Package          Version   Synopsis
[ ] emacs-vterm    0.0.2     Fully-fledged terminal emulator inside GNU Emacs
[I] emacs-magit    3.3.0     It's Magit! A Git porcelain inside Emacs
[ ] emacs-corfu    0.35      Completion Overlay Region Function
[D] emacs-company  0.9.13    Modular in-buffer completion framework
```

Inside this buffer, you can navigate using standard Dired-like keystrokes:

  - `i`: Mark the package at point for **installation**.
  - `d`: Mark the package at point for **deletion**.
  - `u`: Mark the package at point for **upgrade**.
  - `x`: **Execute!** Applies all marked transactions in a single atomic Guix profile transaction.
  - `Return`: Open a detailed package card displaying its synopsis, full description, direct dependencies, licenses, and store outputs.

#### Visualizing and Diffing Generations

Run `M-x guix-generations`. Emacs displays your entire profile history:
```bash
Generation 41  2026-11-12 09:14:22
Generation 42  2026-11-13 18:30:05
Generation 43  (current) 2026-11-14 01:15:00
```

Place your cursor on Generation 42 and press **`d`** (`guix-generation-diff`) against Generation 43. Emacs splits the window and displays a clean diff:
```bash
Packages added:
  ripgrep  13.0.0
Packages upgraded:
  gcc-toolchain  11.3.0 -> 12.2.0
Packages removed:
  vim-tiny 8.2
```

You can visually track the exact evolution of your workstation over months of use.

#### System Reconfiguration from Within Emacs

You don't even need to leave Emacs to update your operating system:

`M-x guix-system-reconfigure`

Emacs prompts for your `config.scm` path, executes the build with root permissions, and streams the live build logs into an interactive compilation buffer!

### Project Isolation: `guix shell` meets `envrc-mode`

One of the greatest headaches for modern software developers is managing conflicting language servers, linters, and compiler versions across multiple repositories:

  - Repository A requires Python 3.9 with `pyright` and `black` 22.0.
  - Repository B requires Python 3.11 with `ruff` and `mypy`.
  - Repository C requires a specific Rust nightly toolchain with `rust-analyzer`.

In traditional setups, developers either litter their home directories with `nvm`, `pyenv`, and `rustup`, or struggle to configure complex editor extensions.

In the Guix + Emacs ecosystem, this problem has a flawless, zero-friction solution: **`guix shell` paired with `envrc-mode`**.

#### The 3-Step Setup

  - **Declare the Project Manifest (`manifest.scm`)**:
    Inside your project directory, declare the exact tools required:
```scheme
;; manifest.scm in project root
    (specifications->manifest
      '("python@3.11"
        "python-pytest"
        "python-requests"
        "python-lsp-server"))
```

  - **Create the `.envrc` File**:
    In the same directory, add a one-line `.envrc` file:
```bash
# .envrc
    eval "$(guix shell -m manifest.scm --search-paths)"
```

  - **Enable `envrc-mode` in Emacs**:
    Install `emacs-envrc` via Guix and add this hook to your `init.el`:
```scheme
(use-package envrc
      :hook (after-init . envrc-global-mode))
```

#### The Magic in Action

The moment you switch to a buffer containing a file from Repository A, `envrc-mode` intercepts the buffer and sets its buffer-local `exec-path` and `process-environment` to match the Guix shell!

When Emacs launches a language server (via `eglot` or `lsp-mode`), it doesn't search your global operating system. It automatically launches the exact `python-lsp-server` or `rust-analyzer` provisioned inside that repository's hermetic store closure.

When you switch to a buffer in Repository B, Emacs instantly shifts to that project's compiler and tools. You never have to manually activate virtualenvs, export environment variables, or restart your editor again.

### The Ultimate Lisp Desktop: EXWM on Guix System

For those who wish to achieve computing nirvana, GNU Guix System offers built-in support for **EXWM** (the Emacs X Window Manager).

Under EXWM, there is no GNOME, no KDE, no XFCE, and no Sway. **Emacs is your window manager.**
```scheme
;; In /etc/config.scm
(use-modules (gnu)
             (gnu services desktop)
             (gnu packages emacs-xyz))

(operating-system
  ;; ...
  (services
    (cons* (service exwm-service-type
             (exwm-configuration
               (package emacs-exwm)))
           %desktop-services)))
```

When your computer boots:

  - X11 starts and hands display management directly to GNU Emacs.
  - Every external application you open—Firefox, LibreOffice, GIMP, MPV—becomes a standard Emacs buffer!
  - You switch between a C source file, an IRC chat, a terminal, and a YouTube video in Firefox using the exact same keystrokes: `C-x b` (`switch-to-buffer`).
  - You can split windows, save layouts, and apply macros across all applications uniformly.

Your entire digital existence becomes a single, unified, navigable Lisp expression.

### Summary: An Unbreakable Alliance

GNU Guix and GNU Emacs are not merely compatible programs; they are two halves of the same grand vision:

  - **Guix protects Emacs**: It liberates Emacs from mutable distribution chaos, pre-compiles native C dependencies without hassle, and enables atomic rollbacks for all your editor extensions.
  - **Emacs elevates Guix**: It provides the living, interactive cockpit where Scheme records are interrogated live, service definitions are navigated with `M-.`, and system generations are browsed visually.

Once you have experienced an operating system where your system configuration, your package manager, your init system, and your editor all speak the same language, returning to traditional operating systems feels like returning to the stone age. 

Welcome to the Living Lisp Machine.

[⬆ Back to Table of Contents](#-table-of-contents)



---

# Appendices



## Appendix A: The Ultimate Guix Cheat Sheet

### Daily Package Management

| **Command** | **Description** |
| :--- | :--- |
| `guix search <query>` | Search available packages by name and description |
| `guix show <pkg>` | Display detailed package metadata and store hash |
| `guix install <pkg>` | Install one or more packages into active profile |
| `guix remove <pkg>` | Remove packages from active profile |
| `guix upgrade` | Upgrade all installed packages to latest versions |
| `guix package –roll-back` | Instantly roll back user profile to previous generation |
| `guix package -l` | List all profile generations and timeline |
| `guix package -S <gen>` | Switch directly to a specific generation number |
| `guix gc` | Run garbage collection to delete unreferenced store items |
| `guix gc -F 10G` | Reclaim disk space until at least 10GB is free |

### Development with `guix shell`

| **Command** | **Description** |
| :--- | :--- |
| `guix shell pkg1 pkg2` | Enter temporary shell with specified packages |
| `guix shell –pure pkg1` | Enter isolated shell stripping host environment vars |
| `guix shell -C -N pkg1` | Enter unprivileged Linux container with networking |
| `guix shell -D <pkg>` | Enter shell with all build dependencies of package |
| `guix shell -m manifest.scm` | Load environment defined in a Scheme manifest |
| `guix shell –expose=/data` | Mount host directory read-only inside container |
| `guix shell –share=/work` | Mount host directory read-write inside container |

### Package Transformations

| **Transformation Flag** | **Effect** |
| :--- | :--- |
| `–with-source=pkg=tarball` | Replace upstream source with local archive/dir |
| `–with-branch=pkg=main` | Fetch and build from a specific Git branch |
| `–with-commit=pkg=commit` | Fetch and build from a specific Git commit hash |
| `–with-input=old=new` | Graph rewrite: replace dependency across whole DAG |
| `–with-c-toolchain=pkg=clang` | Recompile package using Clang instead of GCC |
| `–with-debug-info=pkg` | Build and preserve full GDB debugging symbols |

### System, Home, and Shepherd Administration

| **Command** | **Description** |
| :--- | :--- |
| `sudo guix system reconfigure cfg.scm` | Build and apply system configuration |
| `guix system build cfg.scm` | Dry-run test build of system configuration |
| `guix system image -t qcow2 cfg.scm` | Generate bootable QEMU QCOW2 virtual machine |
| `guix home reconfigure home.scm` | Instantiate declarative user dotfiles/env |
| `guix home roll-back` | Roll back user dotfile generation |
| `herd status` | List all running/stopped Shepherd services |
| `sudo herd restart <service>` | Restart a Shepherd background daemon |
| `guix pull` | Update Guix tool and pull latest package definitions |
| `guix describe -f channels` | Export current channel commits to `channels.scm` |
| `guix time-machine -C ch.scm – ...` | Execute commands in a locked historic environment |

### Standalone Bundles and Distribution (`guix pack`)

| **Command** | **Description** |
| :--- | :--- |
| `guix pack -R -S /bin=bin <pkgs>` | Build relocatable tarball with user-namespace / PRoot wrapper |
| `guix pack -f docker -S /bin=bin <pkgs>` | Build reproducible Docker / OCI container image |
| `guix pack -f docker –entry-point=bin/app` | Set default container entry point executable |
| `guix pack -f appimage -S /bin=bin <pkg>` | Build single-file executable AppImage for desktop Linux |
| `guix pack -f squashfs <pkgs>` | Build SquashFS image for Singularity / Apptainer |
| `guix pack -m manifest.scm -f docker` | Pack complete project manifest into Docker image |
| `guix copy –to=user@host <pkg>` | Synchronize package and missing closure over SSH |
| `guix archive –export -r <pkg>` | Export signed closure archive for air-gapped systems |
| `guix archive –import < archive.nar` | Import signed archive directly into local store |

[⬆ Back to Table of Contents](#-table-of-contents)



## Appendix B: Troubleshooting and Common Footguns

> *""Experience is simply the name we give our past build failures.""*
> 
> — **Oscar Wilde (adapted)**

Even the most seasoned functional alchemists occasionally run into a cryptic error or a failed derivation. Here is a curated diagnostic guide for the most common Guix pitfalls.

### Footgun 1: "No such file or directory" on Existing Scripts

> [!NOTE]
> **ℹ️ Diagnostic Information: Symptom**
>
> You run an executable Python or Bash script with `./script.sh` and get:

> ```bash
> bash: ./script.sh: No such file or directory
> ```
>
> even though `ls -l script.sh` shows the file exists and has executable (`+x`) permissions!

**Diagnosis**: The script begins with `#!/bin/bash`, `#!/usr/bin/env`, or `#!/usr/bin/python`, but that interpreter does not exist at that absolute path on a pure Guix system.

**Solution**:

  - In a package definition, let `patch-shebangs` run, or use `search-input-file`:
```scheme
(substitute* "script.sh"
    (("/bin/bash") (search-input-file inputs "/bin/bash")))
```

  - In a development shell, run the script explicitly with the interpreter:
```bash
guix shell python -- python3 ./script.py
```

### Footgun 2: Scheme Error: "Unbound Variable"

> [!NOTE]
> **ℹ️ Diagnostic Information: Symptom**
>
> When running `guix build` or `guix system reconfigure`, you see:

> ```bash
> error: openssl: unbound variable
> hint: Did you forget `(use-modules (gnu packages tls))'?
> ```
>

**Diagnosis**: Guix organizes packages into granular Scheme modules. Unlike Python where global namespace pollution is common, Guile requires you to explicitly import the module that defines the variable.

**Solution**: Add the corresponding module to your `use-modules` or `use-package-modules` header at the top of the file.

### Footgun 3: Test Suite Fails Because of No Network Access

> [!NOTE]
> **ℹ️ Diagnostic Information: Symptom**
>
> A package build fails during the `check` phase with socket or DNS resolution errors (e.g. `getaddrinfo failed`).

**Diagnosis**: The `guix-daemon` executes builds in a network-isolated container to ensure hermetic reproducibility. Upstream test suites that attempt to ping `google.com` or download test fixtures on the fly will fail.

**Solution**:

  - If the tests are non-essential network checks, disable the test phase:
```scheme
(arguments (list #:tests? #f))
```

  - Or use `modify-phases` to disable only the specific offending unit tests:
```scheme
(add-before 'check 'disable-network-tests
    (lambda _
      (setenv "SKIP_NETWORK_TESTS" "1")))
```

### Footgun 4: Disk Space Running Out in `/tmp`

> [!NOTE]
> **ℹ️ Diagnostic Information: Symptom**
>
> Compiling a massive package (like `gcc`, `llvm`, or `chromium`) fails with `No space left on device` while building in `/tmp/guix-build-...`.

**Diagnosis**: The build daemon extracts source trees and object files into `TMPDIR`, which is often mounted on a RAM disk (`tmpfs`) with limited size.

**Solution**: Set `TMPDIR` to a disk directory with ample storage before running the build:
```bash
export TMPDIR=/var/tmp
guix build large-package
```

### Footgun 5: "Why didn't `guix gc` free any space?"

> [!NOTE]
> **ℹ️ Diagnostic Information: Symptom**
>
> You run `guix gc`, but the disk usage of `/gnu/store` barely changes.

**Diagnosis**: Old generations of your user profile, system profile, or custom profiles are still referencing those packages as active GC roots.

**Solution**: First delete old profile generations:
```bash
# Delete old user profile generations
guix package --delete-generations

# Delete old system generations (if using Guix System)
sudo guix system delete-generations

# Reclaim store space
guix gc
```

[⬆ Back to Table of Contents](#-table-of-contents)

---

# Building Offline Editions

If you prefer to read offline or print a physical copy, you can compile both the high-resolution vector PDF and EPUB editions locally using the included `Makefile`.

### System Requirements
- **LaTeX Distribution:** `pdflatex` (TeX Live with standard collections)
- **EPUB Builder:** `pandoc` (v2.19+) and `python3` (v3.8+)
- **Build Automation:** GNU `make`

### Compilation Commands

```bash
# 1. Clone the repository
git clone https://github.com/sudheerkmuhammed/guix.git
cd guix

# 2. Build both PDF and EPUB editions
make all

# 3. Build only the PDF (performs 2 passes for cross-references & TOC)
make pdf

# 4. Build only the EPUB edition
make epub

# 5. Clean auxiliary build files (.aux, .log, .toc)
make clean

# 6. Re-generate this extensive README.md from LaTeX sources
python3 generate_readme.py
```

---

# License

Copyright © 2026 Sudheer K. Mohammed.

This book and its accompanying source code are free documentation: you can redistribute them and/or modify them under the terms of the **GNU General Public License** as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

All package definitions, Scheme manifests, and configurations presented herein are released into the public domain under the **Creative Commons CC0 1.0 Universal Public Domain Dedication**.

[⬆ Back to Table of Contents](#-table-of-contents)
