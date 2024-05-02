import {BaseState} from "./BaseState"
import {IControllee} from "./IControllee"
import {StateController} from "./StateController"
export class StateNotShooting extends BaseState
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
            this.SetupSubState(this._stateController.InstanceOfIdle, resume);
        }
    }
    public TransitEscape(): BaseState | null
    {
        this._controlleeImp.DoAction3();
        this._stateController.InstanceOfEscaped.Setup(false, false);
        return this._stateController.InstanceOfEscaped;
    }
    public TransitEvConfig(): BaseState | null
    {
        let currentSubState: BaseState | null = this.CurrentSubState();
        if(currentSubState != null)
        {
            let nextState: BaseState | null = currentSubState.TransitEvConfig();
            return this.TransitBySubState(nextState);
        }
        return null;
    }
    public GetStateName(): string
    {
        let currentSubState: BaseState | null = this.CurrentSubState();
        if(currentSubState == null)
        {
            return "NotShooting(end)";
        }
        return currentSubState.GetStateName();
    }
    public GetParent(): BaseState | null
    {
        return null;
    }
}