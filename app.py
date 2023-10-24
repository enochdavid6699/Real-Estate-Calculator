import streamlit as st

def main():
    st.title("Real Estate Investment Calculator")

    # Desired Profit (Eg: 30000)
    desired_profit = st.number_input("Desired Profit")

    # Committed Capital (Eg: 9832)
    committed_capital = st.number_input("Committed Capital")

    # Purchase Price (Eg: 96500)
    purchase_price = st.number_input("Purchase Price")

    # Repair Costs (Eg: 40000)
    repair_costs = st.number_input("Repair Cost")

    # Financing Costs (Eg: 10755)
    financing_costs = st.number_input("Financing Cost")

    # Buying Transaction Costs (Eg: 3727)
    buying_transaction_costs = st.number_input("Buying Transaction Cost")

    # Holding Costs (Eg: 3375)
    holding_costs = st.number_input("Holding Costs")

    # Selling Transaction Costs (Eg: 10938)
    selling_transaction_costs = st.number_input("Selling Transaction Cost")

    # Hold Time In Months
    hold_time_months = st.number_input("Hold Time In Months", min_value=1)

    if st.button("Calculate"):
        total_amount_required = desired_profit + committed_capital
        number_of_years = hold_time_months / 12
        buying_rate = (total_amount_required / committed_capital) ** (1 / number_of_years) * 100

        st.write(f"You need to buy the property at a rate of approximately {buying_rate:.2f}% to achieve your desired minimum profit of ${desired_profit}.")

if __name__ == "__main__":
    main()
