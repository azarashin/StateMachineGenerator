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
        console.log("1. Event2");
        console.log("2. Event21");
        console.log("3. Event31");
        console.log("4. Event42");
        console.log("5. Event421");
        console.log("6. Event431");
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
                    this._stateController.TransitEvent2();
                    this.Step();;
                    break;
                case 2:
                    this._stateController.TransitEvent21();
                    this.Step();;
                    break;
                case 3:
                    this._stateController.TransitEvent31();
                    this.Step();;
                    break;
                case 4:
                    this._stateController.TransitEvent42();
                    this.Step();;
                    break;
                case 5:
                    this._stateController.TransitEvent421();
                    this.Step();;
                    break;
                case 6:
                    this._stateController.TransitEvent431();
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