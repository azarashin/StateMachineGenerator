#pragma once

class IControllee
{
public:
    virtual void DoAction1() = 0;
    virtual void DoAction3() = 0;
    virtual void NoTransition(const char* state, const char* transition) = 0;
    virtual void OverTransition(const char* transition) = 0;
};