import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateIdle extends BaseState
{
    private _stateController: StateController;
    private _controlleeImp: IControllee;
    public constructor(stateController: StateController, controllee: IControllee)
    {
        super(controllee);
        this._stateController = stateController;
        this._controlleeImp = controllee;
    }
    public TransitEvConfig(): BaseState | null
    {
        this._controlleeImp.DoAction1();
        this._stateController.InstanceOfConfiguring.Setup(false, false);
        return this._stateController.InstanceOfConfiguring;
    }
    public  GetStateName(): string
    {
        return "NotShooting.Idle";
    }
    public GetParent(): BaseState | null
    {
        return this._stateController.InstanceOfNotShooting;
    }
}