import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class Statelong2 extends BaseState
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
        this._stateController.InstanceOfProcessData.Setup(false, false);
        return this._stateController.InstanceOfProcessData;
    }
    public TransitNewData(): BaseState | null
    {
        this._stateController.InstanceOflong2.Setup(false, false);
        return this._stateController.InstanceOflong2;
    }
    public  GetStateName(): string
    {
        return "State3.State4.long2";
    }
    public GetParent(): BaseState | null
    {
        return this._stateController.InstanceOfState4;
    }
}