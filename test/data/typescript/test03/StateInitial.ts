import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateInitial extends BaseState
{
    private _stateController: StateController;
    private _controlleeImp: IControllee;
    public constructor(stateController: StateController, controllee: IControllee)
    {
        super(controllee);
        this._stateController = stateController;
        this._controlleeImp = controllee;
    }
    public TransitGoInTo(): BaseState | null
    {
        this._controlleeImp.DoAction0();
        this._stateController.InstanceOfNotShooting.Setup(false, false);
        return this._stateController.InstanceOfNotShooting;
    }
    public  GetStateName(): string
    {
        return "Initial";
    }
    public GetParent(): BaseState | null
    {
        return null;
    }
    public GetStateID(): number
    {
        return 3;
    }
}