public interface IControllee
{
    void DoAction1();
    void DoAction2();
    void DoAction3();
    void NoTransition(string state, string transition);
    void OverTransition(string transition);
}