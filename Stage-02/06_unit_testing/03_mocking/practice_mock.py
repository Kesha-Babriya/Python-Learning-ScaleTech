from unittest.mock import Mock

# creates a mock called mock1
mock1 = Mock()

# calls it with 10, 20 args

mock1(10,20)

# prints call_count
print(mock1.call_count)

# prints call_args
print(mock1.call_args)
print(mock1.call_args_list)

#mock 2
mock2 = Mock()
mock2.return_value = 500

result = mock2()

print(result)
mock2(1)
mock2(2)
mock2(3)
print(mock2.call_count)

print(mock2.call_args)      #gives latest call args
print(mock2.call_args_list)     #all call args list


#3 mock

send_email = Mock()

# call with args
send_email("kesha@gmail.com")

send_email.assert_called()  #check if it is called at least one time if not then test fail
send_email.assert_called_once()  #check if it is called only one time if not then test fail
send_email.assert_called_once_with("kesha@gmail.com")  #check upper test with args
send_email.assert_called_with("kesha@gmail.com")  #check upper test with args

#if failed then this error occurs
# raise AssertionError(_error_message()) from cause
# AssertionError: expected call not found.
# Expected: mock('kesha@gmail.co')
#   Actual: mock('kesha@gmail.com')