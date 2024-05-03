import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateState1 extends BaseState
{
    private _stateController: StateController;
    private _controlleeImp: IControllee;
    public constructor(stateController: StateController, controllee: IControllee)
    {
        super(controllee);
        this._stateController = stateController;
        this._controlleeImp = controllee;
    }
    public TransitEvent2(): BaseState | null
    {
        this._controlleeImp.DoAction2();
        this._stateController.InstanceOfState2.Setup(false, false);
        return this._stateController.InstanceOfState2;
    }
    public TransitEvent21(): BaseState | null
    {
        this._controlleeImp.DoAction21();
        this._stateController.InstanceOfState21.Setup(false, false);
        return this._stateController.InstanceOfState21;
    }
    public TransitEvent31(): BaseState | null
    {
        this._controlleeImp.DoAction31();
        this._stateController.InstanceOfState31.Setup(false, false);
        return this._stateController.InstanceOfState31;
    }
    public  GetStateName(): string
    {
        return "State1";
    }
    public GetParent(): BaseState | null
    {
        return null;
    }
    public GetStateID(): number
    {
        return 0;
    }
}