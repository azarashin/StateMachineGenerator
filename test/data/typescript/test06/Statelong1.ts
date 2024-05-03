import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class Statelong1 extends BaseState
{
    private _stateController: StateController;
    private _controlleeImp: IControllee;
    public constructor(stateController: StateController, controllee: IControllee)
    {
        super(controllee);
        this._stateController = stateController;
        this._controlleeImp = controllee;
    }
    public TransitEnoughData(): BaseState | null
    {
        this._stateController.InstanceOfState4.Setup(false, false);
        return this._stateController.InstanceOfState4;
    }
    public TransitNewData(): BaseState | null
    {
        this._stateController.InstanceOflong1.Setup(false, false);
        return this._stateController.InstanceOflong1;
    }
    public  GetStateName(): string
    {
        return "State3.long1";
    }
    public GetParent(): BaseState | null
    {
        return this._stateController.InstanceOfState3;
    }
    public GetStateID(): number
    {
        return 5;
    }
}