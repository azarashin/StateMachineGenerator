#pragma once
class IControllee
{
public:
    virtual void DoSaveResult() = 0;
    virtual void NoTransition(const char* state, const char* transition) = 0;
    virtual void OverTransition(const char* transition) = 0;
};