#pragma once
class IControllee
{
public:
    virtual void DoAction2() = 0;
    virtual void DoAction21() = 0;
    virtual void DoAction31() = 0;
    virtual void DoAction42() = 0;
    virtual void DoAction421() = 0;
    virtual void DoAction431() = 0;
    virtual void NoTransition(const char* state, const char* transition) = 0;
    virtual void OverTransition(const char* transition) = 0;
};