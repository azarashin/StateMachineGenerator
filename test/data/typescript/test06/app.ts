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
        console.log("1. Aborted");
        console.log("2. DeepResume");
        console.log("3. EnoughData");
        console.log("4. Failed");
        console.log("5. NewData");
        console.log("6. Pause");
        console.log("7. Resume");
        console.log("8. Succeeded");
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
                    this._stateController.TransitAborted();
                    this.Step();;
                    break;
                case 2:
                    this._stateController.TransitDeepResume();
                    this.Step();;
                    break;
                case 3:
                    this._stateController.TransitEnoughData();
                    this.Step();;
                    break;
                case 4:
                    this._stateController.TransitFailed();
                    this.Step();;
                    break;
                case 5:
                    this._stateController.TransitNewData();
                    this.Step();;
                    break;
                case 6:
                    this._stateController.TransitPause();
                    this.Step();;
                    break;
                case 7:
                    this._stateController.TransitResume();
                    this.Step();;
                    break;
                case 8:
                    this._stateController.TransitSucceeded();
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