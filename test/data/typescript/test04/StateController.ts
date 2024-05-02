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
    readonly InstanceOfConfiguring: BaseState;
    readonly InstanceOfEscaped: BaseState;
    readonly InstanceOfIdle: BaseState;
    readonly InstanceOfInitial: BaseState;
    readonly InstanceOfNotShooting: BaseState;
    public constructor(controllee: IControllee)
    {
        this._controllee = controllee;
        this.InstanceOfConfiguring = new StateConfiguring(this, this._controllee);
        this.InstanceOfEscaped = new StateEscaped(this, this._controllee);
        this.InstanceOfIdle = new StateIdle(this, this._controllee);
        this.InstanceOfInitial = new StateInitial(this, this._controllee);
        this.InstanceOfNotShooting = new StateNotShooting(this, this._controllee);
        this._currentState = this.InstanceOfInitial;
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