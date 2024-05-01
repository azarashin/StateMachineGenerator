public interface IControllee
{
    void DoAction0();
    void DoAction1();
    void DoAction2();
    void DoAction3();
    void NoTransition(string state, string transition);
    void OverTransition(string transition);
}