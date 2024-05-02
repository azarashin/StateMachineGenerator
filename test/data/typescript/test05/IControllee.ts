export interface IControllee
{
    DoAction2(): void
    DoAction21(): void
    DoAction31(): void
    DoAction42(): void
    DoAction421(): void
    DoAction431(): void
    NoTransition(state: string, transition: string): void
    OverTransition(transition: string): void
}