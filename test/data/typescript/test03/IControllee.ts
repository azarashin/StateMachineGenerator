export interface IControllee
{
    DoAction0(): void
    DoAction1(): void
    DoAction2(): void
    DoAction3(): void
    NoTransition(state: string, transition: string): void
    OverTransition(transition: string): void
}