import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateState3 extends BaseState
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
            this.SetupSubState(this._stateController.InstanceOflong1, resume);
        }
    }
    public TransitAborted(): BaseState | null
    {
        return null;
    }
    public TransitFailed(): BaseState | null
    {
        this._stateController.InstanceOfState3.Setup(false, false);
        return this._stateController.InstanceOfState3;
    }
    public TransitPause(): BaseState | null
    {
        this._stateController.InstanceOfState2.Setup(false, false);
        return this._stateController.InstanceOfState2;
    }
    public TransitSucceeded(): BaseState | null
    {
        this._controlleeImp.DoSaveResult();
        return null;
    }
    public TransitEnoughData(): BaseState | null
    {
        let currentSubState: BaseState | null = this.CurrentSubState();
        if(currentSubState != null)
        {
            let nextState: BaseState | null = currentSubState.TransitEnoughData();
            return this.TransitBySubState(nextState);
        }
        return null;
    }
    public TransitNewData(): BaseState | null
    {
        let currentSubState: BaseState | null = this.CurrentSubState();
        if(currentSubState != null)
        {
            let nextState: BaseState | null = currentSubState.TransitNewData();
            return this.TransitBySubState(nextState);
        }
        return null;
    }
    public GetStateName(): string
    {
        let currentSubState: BaseState | null = this.CurrentSubState();
        if(currentSubState == null)
        {
            return "State3(end)";
        }
        return currentSubState.GetStateName();
    }
    public GetParent(): BaseState | null
    {
        return null;
    }
}