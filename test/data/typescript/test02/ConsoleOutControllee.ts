import {IControllee} from "./IControllee"
export class ConsoleOutControllee implements IControllee
{
    public DoAction1(): void
    {
        console.log("Action1");
    }
    public DoAction3(): void
    {
        console.log("Action3");
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