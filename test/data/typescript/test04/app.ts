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
        console.log("-1. ShowStateIDs then resume");
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
                case -1:
                {
                    let stateId: number = this._stateController.GetCurrentIdFromStateId(-1);
                    console.log(`Top State ID: ${stateId} - ${this._stateController.StateName(stateId)}`);
                    let subStateIds: number[] = new Array(this._stateController.MaxNumberOfStateIDs);
                    for(let i: number = 0;i<this._stateController.MaxNumberOfStateIDs;i++)
                    {
                        subStateIds[i] = this._stateController.GetCurrentIdFromStateId(i);
                        console.log(`Sub State ID: ${subStateIds[i]} - ${this._stateController.StateName(subStateIds[i])}`);
                    }
                    this._stateController = new StateController( new ConsoleOutControllee());
                    console.log(`StateController has been reset.`);
                    this._stateController.ResumeState(-1, stateId);
                    for(let i: number = 0;i<this._stateController.MaxNumberOfStateIDs;i++)
                    {
                        this._stateController.ResumeState(i, subStateIds[i]);
                    }
                    stateId = this._stateController.GetCurrentIdFromStateId(-1);
                    console.log(`Top State ID: ${stateId} - ${this._stateController.StateName(stateId)}`);
                    for(let i: number = 0;i<this._stateController.MaxNumberOfStateIDs;i++)
                    {
                        subStateIds[i] = this._stateController.GetCurrentIdFromStateId(i);
                        console.log(`Sub State ID: ${subStateIds[i]} - ${this._stateController.StateName(subStateIds[i])}`);
                    }
                }
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