import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateConfiguring extends BaseState
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
        this._controlleeImp.DoAction2();
        this._stateController.InstanceOfIdle.Setup(false, false);
        return this._stateController.InstanceOfIdle;
    }
    public  GetStateName(): string
    {
        return "NotShooting.Configuring";
    }
    public GetParent(): BaseState | null
    {
        return this._stateController.InstanceOfNotShooting;
    }
}