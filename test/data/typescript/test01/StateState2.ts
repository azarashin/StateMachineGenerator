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
    public TransitCommand3(): BaseState | null
    {
        this._controlleeImp.DoAction3();
        return null;
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
        return 1;
    }
}