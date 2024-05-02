import {IControllee} from "./IControllee"
import {BaseState} from "./BaseState"
import {StateProcessData} from "./StateProcessData"
import {StateState1} from "./StateState1"
import {StateState2} from "./StateState2"
import {StateState3} from "./StateState3"
import {StateState4} from "./StateState4"
import {Statelong1} from "./Statelong1"
import {Statelong2} from "./Statelong2"
export class StateController
{
    private  _controllee: IControllee;
    private _currentState: BaseState | null;
    readonly InstanceOfProcessData: BaseState;
    readonly InstanceOfState1: BaseState;
    readonly InstanceOfState2: BaseState;
    readonly InstanceOfState3: BaseState;
    readonly InstanceOfState4: BaseState;
    readonly InstanceOflong1: BaseState;
    readonly InstanceOflong2: BaseState;
    public constructor(controllee: IControllee)
    {
        this._controllee = controllee;
        this.InstanceOfProcessData = new StateProcessData(this, this._controllee);
        this.InstanceOfState1 = new StateState1(this, this._controllee);
        this.InstanceOfState2 = new StateState2(this, this._controllee);
        this.InstanceOfState3 = new StateState3(this, this._controllee);
        this.InstanceOfState4 = new StateState4(this, this._controllee);
        this.InstanceOflong1 = new Statelong1(this, this._controllee);
        this.InstanceOflong2 = new Statelong2(this, this._controllee);
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
    public TransitAborted(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitAborted();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Aborted");
        }
    }
    public TransitDeepResume(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitDeepResume();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("DeepResume");
        }
    }
    public TransitEnoughData(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitEnoughData();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("EnoughData");
        }
    }
    public TransitFailed(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitFailed();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Failed");
        }
    }
    public TransitNewData(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitNewData();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("NewData");
        }
    }
    public TransitPause(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitPause();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Pause");
        }
    }
    public TransitResume(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitResume();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Resume");
        }
    }
    public TransitSucceeded(): void
    {
        if(this._currentState != null)
        {
            this._currentState = this._currentState.TransitSucceeded();
            if(this._currentState != null)
            {
                this._currentState = this._currentState.OutlineState();
            }
        } else {
            this._controllee.OverTransition("Succeeded");
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