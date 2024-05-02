import {IControllee} from "./IControllee"
export abstract class BaseState
{
    private _controllee: IControllee;
    private _currentSubState: BaseState | null;
    public constructor(controllee: IControllee)
    {
        this._controllee = controllee;
        this._currentSubState = null;
    }
    public Setup(resume: boolean, deepResume: boolean): void
    {
        return;
    }
    public TransitEscape(): BaseState | null
    {
        this._controllee.NoTransition(this.GetStateName(), "Escape");
        return this;
    }
    public TransitEvConfig(): BaseState | null
    {
        this._controllee.NoTransition(this.GetStateName(), "EvConfig");
        return this;
    }
    public TransitGoInTo(): BaseState | null
    {
        this._controllee.NoTransition(this.GetStateName(), "GoInTo");
        return this;
    }
    public TryTransitWithoutEvent(): BaseState
    {
        return this;
    }
    public SetupSubState(child: BaseState, resume: boolean): void
    {
        if(!resume)
        {
            this._currentSubState = child;
        }
        if(this._currentSubState != null)
        {
            this._currentSubState.Setup(false, false);
        }
    }
    public CurrentSubState(): BaseState | null
    {
        return this._currentSubState;
    }
    public TransitBySubState(nextState: BaseState | null): BaseState | null
    {
        if(nextState == null || this._currentSubState == null)
        {
            return nextState;
        }
        let parentOfNextState: BaseState | null = this._currentSubState.GetParent();
        let parentOfCurrentState: BaseState | null = nextState.GetParent();
        if(parentOfNextState != null && parentOfCurrentState != null && parentOfNextState == parentOfCurrentState)
        {
            this._currentSubState = nextState;
            return this;
        }
        return nextState;
    }
    public TransitForChild(child: BaseState): BaseState
    {
        this._currentSubState = child;
        let parent: BaseState | null = this.GetParent();
        if(parent != null)
        {
            return parent.TransitForChild(this);
        }
        return this;
    }
    public OutlineState(): BaseState
    {
        let parent: BaseState | null = this.GetParent();
        if(parent != null)
        {
            return parent.TransitForChild(this);
        }
        return this;
    }
    public abstract GetStateName(): string;
    public abstract GetParent(): BaseState | null;
}