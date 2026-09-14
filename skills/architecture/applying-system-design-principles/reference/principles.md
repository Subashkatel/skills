# The principles, with sources

Line numbers refer to the plain text extracted from each source with
pypdf (page markers `=== PAGE n ===` included) or from the HTML with
tags stripped; line numbers identify that extraction only and can change on re-extraction.
Verify the document revision, section/page, and quoted passage. Where to get each source is listed at the end. Quote the
sentence when citing, never only the number.

The source passages are distinct from the proposed checks below. Checks are
heuristics; decsim-specific policies come from the active worktree's `STYLE.md`.

## 1. A module hides one design decision likely to change (Parnas 1972)

"We propose instead that one begins with a list of difficult design
decisions or design decisions which are likely to change. Each module
is then designed to hide such a decision from the others" (lines
547-550). "It is almost always incorrect to begin the decomposition of
a system into modules on the basis of a flowchart" (545-546). "Its
interface or definition was chosen to reveal as little as possible
about its inner workings" (353-355).

Check: the changeability list; one owner per decision.

## 2. "Uses" is a partial order; prune the top and the rest runs (Parnas 1972; Dijkstra 1968)

"We have a hierarchical structure if a certain relation may be defined
between the modules or programs and that relation is a partial
ordering. The relation we are concerned with is 'uses' or 'depends
upon'" (Parnas 505-511). "We are able to cut off the upper levels and
still have a usable and useful product" (518-520). Dijkstra's THE
system: levels 0 to 5, each introducing one abstraction the levels
above rely on (dijkstra_the.txt 52-57); "Starting at level 0 the
system has been tested, each time adding (a portion of) the next level
only after the previous level has been thoroughly tested" (62).

Check: where layering is intended, inspect semantic dependencies and whether
lower levels work independently. An acyclic import graph alone does not prove
information hiding. The bundled absolute-import scan has incomplete coverage.

## 3. Never promise an order that is not needed (Parnas 1972)

"By prescribing the order for the shifts we have given more
information than necessary and so unnecessarily restricted the class
of systems that we can build without changing the definitions ... must
clearly be classified as a design error" (370-379).

Check: avoid pinning incidental order, preserving multiplicity with a multiset
when duplicates are observable.

## 4. An interface is the set of assumptions two programs make about each other (Lampson 1983)

"The interface between two programs consists of the set of assumptions
that each programmer needs to make about the other program in order to
demonstrate the correctness of his program" (79-81). "Do one thing at
a time, and do it well. An interface should capture the minimum
essentials of an abstraction. Don't generalize; generalizations are
generally wrong" (100-101). "If there are six levels of abstraction,
and each costs 50% more than is 'reasonable', the service delivered at
the top will miss by more than a factor of 10" (149-151). "Keep basic
interfaces stable" (362-363). "Keep secrets of the implementation.
Secrets are assumptions about an implementation that client programs
are not allowed to make" (415-416). Also: "Don't hide power" (298),
"Leave it to the client" (337), "Handle normal and worst cases
separately ... The normal case must be fast. The worst case must make
some progress" (496-499), "Split resources in a fixed way if in doubt"
(566).

Check: interfaces have real consumers or justified extension contracts, reveal
only needed assumptions, and have understood costs. Frozen port files and timing
in commit messages are decsim policies, not universal consequences.

## 5. Log updates as functions of their arguments (Lampson 1983)

"The update procedure must be a true function: Its result does not
depend on any state outside its arguments" (947-948); a replayed log
"produce[s] the same objects that were produced in the original
execution" (943-945).

Check: a run is a function of (config, seed); anything priced from a
wall clock is compared on a projection that excludes it.

## 6. gem5's shape (Lowe-Power et al. 2020; gem5 source)

"the user writes a Python script that describes the system under test
by instantiating model objects (SimObjects in gem5 terminology). Each
object has a number of parameters" (342-346). "gem5 provides a modular
port interface which allows any component that implements the port
API to be connected to any other component implementing the same API"
(489-491). "gem5 separates the functional execution from the timing in
most of its models" (369-370). Backpressure "is implemented by a retry
phase" (1620-1621). A SimObject class owns `_params` and `_ports`
(src/python/m5/SimObject.py 204-205). Statistics are one Group per
object mirroring the object hierarchy (src/base/stats/group.hh 60-92).
A response port holds a packet until the far side accepts it
(src/mem/port.hh, sendTimingReq's contract, around 244-255).

Check: assess component-owned settings, separate wiring, function/timing
separation, and observation ownership where those choices suit the simulator.
Inspect class-based plug-in branches for leakage, using local exemptions.

## 7. Shared records in one place; internals never leave (Parnas 1972)

"A data structure, its internal linkings, accessing procedures and
modifying procedures are part of a single module. They are not shared
by many modules as is conventionally done" (384-387).

Check: inspect affected imports for private-state or representation leakage.
The port/record taxonomy and shared-record directory are decsim conventions.

## 8. Layers change at different rates; every observable behaviour gets depended on (Foote and Yoder; Hyrum)

Shearing Layers: "Different artifacts change at different rates"
(bigballofmud.txt 1689-1690; Brand's six layers and lifetimes
1665-1679). Hyrum: "With a sufficient number of users of an API, it
does not matter what you promise in the contract: all observable
behaviors of your system will be depended on by somebody" (hyrum.txt
6-9); "if an interface has enough consumers, they will collectively
depend on every aspect of the implementation" (12).

Check: add a row from outside the package touching no port and no
root line; tests pin only promises.

## 9. Essential versus accidental; grow, do not build; buy what exists (Brooks 1986)

"The complexity of software is an essential property, not an
accidental one" (113). A high-level language "frees a program from
much of its accidental complexity" (206-207). "the system should first
be made to run, even though it does nothing useful except call the
proper set of dummy subprograms. Then, bit-by-bit it is fleshed out"
(660-663). "The most radical possible solution for constructing
software is not to construct it at all" (547-548).

Check: make relevant state explicit, remove complexity without a current
purpose, and assess existing tools. No class size or state representation is
universally implied by this source.

## 10. The system copies the organisation (Conway 1968)

"organizations which design systems ... are constrained to produce
designs which are copies of the communication structures of these
organizations" (117). "Ways must be found to reward design managers
for keeping their organizations lean and flexible" (119). A branch
between two subsystems is a negotiation between two design groups
(78-83).

Check: compare interface ownership with actual coordination needs. A single
implementer and read-only reviewers are workflow choices, not Conway's law.

## 11. Local and remote calls differ in kind, and the interface must say so (Waldo, Wyant, Wollrath, Kendall 1994)

"The major differences between local and distributed computing concern
the areas of latency, memory access, partial failure, and concurrency"
(302-304). "the difference in latency ... is only the most obvious
difference" (382-383). "Being robust in the face of partial failure
requires some expression at the interface level. Merely improving the
implementation of one component is not sufficient" (546-548). "In the
design of any operation, the question has to be asked: what happens if
the client chooses to repeat this operation with the exact same
parameters as previously?" (714-717). "Many aspects of robustness can
be reflected only at the protocol/interface level" (684-685). NFS:
"The problem can be traced to the interface upon which NFS is built,
an interface that was designed for non-distributed computing where
partial failure was not possible" (802-806). "an additional part of
the definition of a class of objects will be the specification of
whether those objects are meant to be used locally or remotely"
(852-855); "There will be a line where the object model changes"
(923-924). Middle ground: objects in different address spaces on one
machine share a resource manager, so partial failure can be avoided
and only latency and memory access differ (948-961).

Check: state which latency, memory, failure, and concurrency differences apply
at the boundary. Record deliberate exclusions. A simulated same-unit operation
may have a modeled cost; pricing alone does not define a distributed system.

## Sources and where to get them

- Parnas, On the Criteria To Be Used in Decomposing Systems into
  Modules, CACM 1972: https://www.win.tue.nl/~wstomv/edu/2ip30/references/criteria_for_modularization.pdf
- Lampson, Hints for Computer System Design, 1983:
  https://bwlampson.site/33-Hints/Acrobat.pdf
- Dijkstra, The Structure of the THE Multiprogramming System, 1968:
  https://www.cs.utexas.edu/~EWD/transcriptions/EWD01xx/EWD196.html
- Conway, How Do Committees Invent, 1968:
  https://www.melconway.com/Home/Committees_Paper.html
- Brooks, No Silver Bullet, 1986:
  http://worrydream.com/refs/Brooks-NoSilverBullet.pdf
- Lowe-Power et al., The gem5 Simulator: Version 20.0+, arXiv
  2007.03152; gem5 source at https://github.com/gem5/gem5
- Hyrum's law: https://www.hyrumslaw.com/
- Foote and Yoder, Big Ball of Mud: http://www.laputan.org/mud/mud.html
- Waldo, Wyant, Wollrath, Kendall, A Note on Distributed Computing,
  SMLI TR-94-29, 1994:
  https://decomposition.al/CSE232-2024-09/readings/note-distributed-computing.pdf
- Local supplementary sources: `saltzer_ch1.pdf` (chapter 1 only),
  `ousterhout_cs190.txt`, and `ousterhout_talk.txt` in the architecture
  corpus. These are not the full books. Check availability before use.
- Liskov and Zilles, Programming with Abstract Data Types: not verified
  in this local corpus during this audit.

Extraction: `python -c "from pypdf import PdfReader; ..."` writing
`=== PAGE n ===` before each page's text, or strip HTML tags and
collapse blank lines. A local copy of the texts used to set these line
numbers lives in the qlx-qec-sandbox at tmp/papers/architecture/.
