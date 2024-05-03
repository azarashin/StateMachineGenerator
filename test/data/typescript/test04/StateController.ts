import {IControllee} from "./IControllee"
import {BaseState} from "./BaseState"
import {StateConfiguring} from "./StateConfiguring"
import {StateEscaped} from "./StateEscaped"
import {StateIdle} from "./StateIdle"
import {StateInitial} from "./StateInitial"
import {StateNotShooting} from "./StateNotShooting"
export class StateController
{
    private  _controllee: IControllee;
    private _currentState: BaseState | null;
    private _stateList: BaseState[];
    readonly InstanceOfConfiguring: BaseState;
    readonly InstanceOfEscaped: BaseState;
    readonly InstanceOfIdle: BaseState;
    readonly InstanceOfInitial: BaseState;
    readonly InstanceOfNotShooting: BaseState;
    readonly MaxNumberOfStateIDs: number = 5;
    public constructor(controllee: IControllee)
    {
        this._controllee = controllee;
        this.InstanceOfConfiguring = new StateConfiguring(this, this._controllee);
        this.InstanceOfEscaped = new StateEscaped(this, this._controllee);
        this.InstanceOfIdle = new StateIdle(this, this._controllee);
        this.InstanceOfInitial = new StateInitial(this, this._controllee);
        this.InstanceOfNotShooting = new StateNotShooting(this, this._controllee);
        this._currentState = this.InstanceOfInitial;
        this._stateList = [
            this.InstanceOfConfiguring,
            this.InstanceOfEscaped,
            this.InstanceOfIdle,
            this.InstanceOfInitial,
            this.InstanceOfNotShooting
        ];
    }
    public GetCurrentIdFromStateId(parentStateId: number): number
    {
        if(parentStateId == -1)
        {
            return this.GetCurrentIdFromState(this._currentState);
        }
        if(parentStateId < -1 || parentStateId >= this.MaxNumberOfStateIDs)
        {
            return -1;
        }
        return this.GetCurrentIdFromState(this._stateList[parentStateId].CurrentSubState());
    }
    private GetCurrentIdFromState(state: BaseState | null): number
    {
        if(state == null)
        {
            return -1;
        }
    return state.GetStateID();
    }
    public ResumeState(parentStateId: number, stateId: number): void
    {
        let state: BaseState | null = null;
        if(stateId >= 0 && stateId < this.MaxNumberOfStateIDs)
        {
            state = this._stateList[stateId];
        }
        if(parentStateId == -1)
        {
            this._currentState = state;
            return;
        }
        if(parentStateId < -1 || parentStateId >= this.MaxNumberOfStateIDs)
        {
            return;
        }
        this._stateList[parentStateId].ResumeSubState(state);
    }
    public StateName(parentStateId: number): string
    {
        if(parentStateId >= 0 && parentStateId < this.MaxNumberOfStateIDs)
        {
            return this._stateList[parentStateId].GetStateName();
        }
        return "(None)";
    }
    public TryTransitWithoutEvent(): boolean
    {
        if(this._currentState == null)
        {
            return false;
        }
        let current: BaseState | null = this._currentState;
        this._currentState = this._currentState.TryTransitWithoutEvent();
        if(this._currentState != null)
        {
            this._currentState = this._currentState.OutlineState();
        }
        return (current != this._currentState);
    }
    public TransitEscape(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitEscape();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Escape");
        }
    }
    public TransitEvConfig(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitEvConfig();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("EvConfig");
        }
    }
    public TransitGoInTo(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitGoInTo();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("GoInTo");
        }
    }
    public GetCurrentStateName(): string
    {
        if(this._currentState == null)
        {
            return "(end)";
        }
        else
        {
            return this._currentState.GetStateName();
        }
    }
}