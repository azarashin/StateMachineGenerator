import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateState31 extends BaseState
{
    private _stateController: StateController;
    private _controlleeImp: IControllee;
    public constructor(stateController: StateController, controllee: IControllee)
    {
        super(controllee);
        this._stateController = stateController;
        this._controlleeImp = controllee;
    }
    public TransitEvent431(): BaseState | null
    {
        this._controlleeImp.DoAction431();
        this._stateController.InstanceOfState4.Setup(false, false);
        return this._stateController.InstanceOfState4;
    }
    public  GetStateName(): string
    {
        return "State2.State21.State31";
    }
    public GetParent(): BaseState | null
    {
        return this._stateController.InstanceOfState21;
    }
    public GetStateID(): number
    {
        return 3;
    }
}