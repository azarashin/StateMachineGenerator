export interface IControllee
{
    DoSaveResult(): void
    NoTransition(state: string, transition: string): void
    OverTransition(transition: string): void
}