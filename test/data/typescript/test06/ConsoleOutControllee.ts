import {IControllee} from "./IControllee"
export class ConsoleOutControllee implements IControllee
{
    public DoSaveResult(): void
    {
        console.log("SaveResult");
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