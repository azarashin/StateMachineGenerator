import {IControllee} from "./IControllee"
import {BaseState} from "./BaseState"
import {StateState1} from "./StateState1"
import {StateState2} from "./StateState2"
import {StateState21} from "./StateState21"
import {StateState31} from "./StateState31"
import {StateState4} from "./StateState4"
export class StateController
{
    private  _controllee: IControllee;
    private _currentState: BaseState | null;
    private _stateList: BaseState[];
    readonly InstanceOfState1: BaseState;
    readonly InstanceOfState2: BaseState;
    readonly InstanceOfState21: BaseState;
    readonly InstanceOfState31: BaseState;
    readonly InstanceOfState4: BaseState;
    readonly MaxNumberOfStateIDs: number = 5;
    public constructor(controllee: IControllee)
    {
        this._controllee = controllee;
        this.InstanceOfState1 = new StateState1(this, this._controllee);
        this.InstanceOfState2 = new StateState2(this, this._controllee);
        this.InstanceOfState21 = new StateState21(this, this._controllee);
        this.InstanceOfState31 = new StateState31(this, this._controllee);
        this.InstanceOfState4 = new StateState4(this, this._controllee);
        this._currentState = this.InstanceOfState1;
        this._stateList = [
            this.InstanceOfState1,
            this.InstanceOfState2,
            this.InstanceOfState21,
            this.InstanceOfState31,
            this.InstanceOfState4
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
    public TransitEvent2(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitEvent2();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Event2");
        }
    }
    public TransitEvent21(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitEvent21();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Event21");
        }
    }
    public TransitEvent31(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitEvent31();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Event31");
        }
    }
    public TransitEvent42(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitEvent42();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Event42");
        }
    }
    public TransitEvent421(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitEvent421();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Event421");
        }
    }
    public TransitEvent431(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitEvent431();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Event431");
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