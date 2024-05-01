public interface IControllee
{
    void DoAction2();
    void DoAction21();
    void DoAction31();
    void DoAction42();
    void DoAction421();
    void DoAction431();
    void NoTransition(string state, string transition);
    void OverTransition(string transition);
}