class MinStack {

private:
    stack<int> values;
    // Add anything else needed to track the minimum.
    stack<int> mins;

public:
    MinStack() {
        // auto initialized
    }
    
    void push(int val) {
        values.push(val);

        // add to min stack

        if (mins.empty() || val <= mins.top()){
            mins.push(val);
        }
        else{
            mins.push(mins.top());
        }
    }
    
    void pop() {
        values.pop();
        mins.pop();
    }
    
    int top() {
        return values.top();
    }
    
    int getMin() {
        return mins.top();
    }
};
