export interface IControllee
{
    DoAction1(): void
    DoAction3(): void
    NoTransition(state: string, transition: string): void
    OverTransition(transition: string): void
}