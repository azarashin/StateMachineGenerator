import {IControllee} from "./IControllee"
export class ConsoleOutControllee implements IControllee
{
    public DoAction2(): void
    {
        console.log("Action2");
    }
    public DoAction21(): void
    {
        console.log("Action21");
    }
    public DoAction31(): void
    {
        console.log("Action31");
    }
    public DoAction42(): void
    {
        console.log("Action42");
    }
    public DoAction421(): void
    {
        console.log("Action421");
    }
    public DoAction431(): void
    {
        console.log("Action431");
    }
    public NoTransition(state: string, transition: string): void
    {
        console.log(`NoTransition(${state}: ${transition})`);
    }
    public OverTransition(transition: string): void
    {
        console.log(`OverTransition(${transition})`);
    }
}