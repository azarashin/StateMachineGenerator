import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateState21 extends BaseState
{
    private _stateController: StateController;
    private _controlleeImp: IControllee;
    public constructor(stateController: StateController, controllee: IControllee)
    {
        super(controllee);
        this._stateController = stateController;
        this._controlleeImp = controllee;
    }
    public Setup(resume: boolean, deepResume: boolean): void
    {
        if(!deepResume)
        {
            this.SetupSubState(this._stateController.InstanceOfState31, resume);
        }
    }
    public TransitEvent421(): BaseState | null
    {
        this._controlleeImp.DoAction421();
        this._stateController.InstanceOfState4.Setup(false, false);
        return this._stateController.InstanceOfState4;
    }
    public TransitEvent431(): BaseState | null
    {
        let currentSubState: BaseState | null = this.CurrentSubState();
        if(currentSubState != null)
        {
            let nextState: BaseState | null = currentSubState.TransitEvent431();
            return this.TransitBySubState(nextState);
        }
        return null;
    }
    public GetStateName(): string
    {
        let currentSubState: BaseState | null = this.CurrentSubState();
        if(currentSubState == null)
        {
            return "State2.State21(end)";
        }
        return currentSubState.GetStateName();
    }
    public GetParent(): BaseState | null
    {
        return this._stateController.InstanceOfState2;
    }
    public GetStateID(): number
    {
        return 2;
    }
}