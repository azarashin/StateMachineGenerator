import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
/// <summary>
/// this is a string
/// this is another string
/// </summary>
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
    public TransitCommand1(): BaseState | null
    {
        this._controlleeImp.DoAction1();
        return null;
    }
    public TransitCommand2(): BaseState | null
    {
        this._controlleeImp.DoAction2();
        this._stateController.InstanceOfState2.Setup();
        return this._stateController.InstanceOfState2;
    }
    public  GetStateName(): string
    {
        return "State1";
    }
    public GetParent(): BaseState | null
    {
        return null;
    }
}