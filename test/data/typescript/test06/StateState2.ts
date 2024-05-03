import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateState2 extends BaseState
{
    private _stateController: StateController;
    private _controlleeImp: IControllee;
    public constructor(stateController: StateController, controllee: IControllee)
    {
        super(controllee);
        this._stateController = stateController;
        this._controlleeImp = controllee;
    }
    public TransitAborted(): BaseState | null
    {
        return null;
    }
    public TransitDeepResume(): BaseState | null
    {
        this._stateController.InstanceOfState3.Setup(true, true);
        return this._stateController.InstanceOfState3;
    }
    public TransitResume(): BaseState | null
    {
        this._stateController.InstanceOfState3.Setup(true, false);
        return this._stateController.InstanceOfState3;
    }
    public TransitSucceeded(): BaseState | null
    {
        this._stateController.InstanceOfState3.Setup(false, false);
        return this._stateController.InstanceOfState3;
    }
    public  GetStateName(): string
    {
        return "State2";
    }
    public GetParent(): BaseState | null
    {
        return null;
    }
    public GetStateID(): number
    {
        return 2;
    }
}