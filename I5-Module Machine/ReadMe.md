# Dataclass - Intro 3.2: Module Machine

In this exerise you will reimplement a solution to the "Implementing Modules" intro exercise from Module 3. However, this time you will use a dataclass model the state a student's progress through a module.

> For this exercise you will implement a state machine that represents a module workflow similar to the one that we are using. The module you'll implement is described by the flow chart below. You should provide input validation each step by printing an error message if the user provides a transition that is invalid.
>
> ![Module workflow](workflow.png)
>
> Here is an example execution:
>
> ```
> Current State: Introductory Exercises
> > Complete
> Current State: Project
> > Pass
> Error: Invalid transition
> Current State: Project
> > Complete
> Current State: Benchmark
> > Fail
> Current State: Project
> > Complete
> Current State: Benchmark
> > Pass
> Current State: Module Complete
> ```

## Rubric

- [ ] `ModuleProgress`, `complete_task`, `pass_task`, and `fail_task` implemented and used correctly.
  - `ModuleProgress` should be a dataclass that has contains the appropriate field(s) to model the state of a student's progress in a module.
  - `complete_task(m: ModuleProgress) -> None` should mutate `m`'s state appropriately for completing the current task.
  - `pass_task(m: ModuleProgress) -> None` should mutate `m`'s state appropriately for passing the current task.
  - `fail_task(m: ModuleProgress) -> None` should mutate `m`'s state appropriately for failing the current task.
- [ ] Correctly models all states and transitions through the state machine.
- [ ] Displays an error message if the user provides an invalid transition.
- [ ] Uses a single `while` loop
- [ ] Uses a branch for each state with nested branches for each transition.

### Style Guide

- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
