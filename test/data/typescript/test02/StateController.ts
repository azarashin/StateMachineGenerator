import {IControllee} from "./IControllee"
import {BaseState} from "./BaseState"
import {StateState1} from "./StateState1"
import {StateState2} from "./StateState2"
export class StateController
{
    private  _controllee: IControllee;
    private _currentState: BaseState | null;
    readonly InstanceOfState1: BaseState;
    readonly InstanceOfState2: BaseState;
    public constructor(controllee: IControllee)
    {
        this._controllee = controllee;
        this.InstanceOfState1 = new StateState1(this, this._controllee);
        this.InstanceOfState2 = new StateState2(this, this._controllee);
        this._currentState = this.InstanceOfState1;
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
    public TransitCommand1(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitCommand1();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Command1");
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