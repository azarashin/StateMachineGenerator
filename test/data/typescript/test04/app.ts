import * as readline from "readline";
import {ConsoleOutControllee} from "./ConsoleOutControllee"
import {StateController} from "./StateController"
class TestApp
{
    private _stateController: StateController = new StateController( new ConsoleOutControllee());
    public Run(): void
    {
        this.Step();
    }
    private Step(): void
    {
        console.log(`current state: ${this._stateController.GetCurrentStateName()}`);
        if(this._stateController.TryTransitWithoutEvent())
        {
            this.Step();
        }
        console.log("1. Escape");
        console.log("2. EvConfig");
        console.log("3. GoInTo");
        console.log("");
        console.log("0. exit");
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        let idStr: string | null = null;
        rl.question('order: ', (answer) => {
            rl.close();
            this.Transit(Number(answer));
        });
    }
    private Transit(id: number): void
    {
        if(id)
        {
            switch(id)
            {
                case 0:
                    break;
                case 1:
                    this._stateController.TransitEscape();
                    this.Step();;
                    break;
                case 2:
                    this._stateController.TransitEvConfig();
                    this.Step();;
                    break;
                case 3:
                    this._stateController.TransitGoInTo();
                    this.Step();;
                    break;
                default:
                    console.log(`Invalid number: ${id}`);
                    this.Step();
                    break;
            }
        }
    }
}
let app: TestApp = new TestApp();
app.Run();