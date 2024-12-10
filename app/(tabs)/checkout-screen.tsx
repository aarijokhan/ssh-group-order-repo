import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Alert, TextInput } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';

type Product = {
  id: string;
  name: string;
  price: number;
  category: string;
};

type GroupMember = {
  name: string;
  cart: Product[];
};

const groupMemberNames: string[] = ["Saad", "Hasaan", "Aarij", "Fizan", "David"];
const DELIVERY_FEE = 5.99;
const SERVICE_FEE = 2.5;

export default function CheckoutScreen() {
  const [products, setProducts] = useState<Product[]>([]);
  const [groupMembers, setGroupMembers] = useState<GroupMember[]>([]);
  const [userCart, setUserCart] = useState<Product[]>([]);
  const [walletBalance, setWalletBalance] = useState<number>(0);
  const [topUpAmount, setTopUpAmount] = useState<string>('');

  useEffect(() => {
    axios
      .get<Product[]>('http://10.115.206.210:8000/products')
      .then((response) => {
        setProducts(response.data);
        generateGroupMembers(response.data);
      })
      .catch(() => Alert.alert('Error', 'Failed to load products.'));

    const fetchCart = async () => {
      const storedCart = await AsyncStorage.getItem('userCart');
      setUserCart(storedCart ? JSON.parse(storedCart) : []);
    };
    fetchCart();
  }, []);

  const generateGroupMembers = (productList: Product[]) => {
    const members: GroupMember[] = groupMemberNames.map((name) => {
      const cart: Product[] = Array.from({ length: Math.floor(Math.random() * 3) + 1 }).map(() => {
        const randomIndex = Math.floor(Math.random() * productList.length);
        return productList[randomIndex];
      });
      return { name, cart };
    });
    setGroupMembers(members);
  };

  const calculateTotal = (cart: Product[]): number => {
    return cart.reduce((sum, item) => sum + item.price, 0);
  };

  const calculateMemberTotal = (cart: Product[]): string => {
    const deliveryShare = DELIVERY_FEE / (groupMembers.length + 1);
    const serviceShare = SERVICE_FEE / (groupMembers.length + 1);
    return (calculateTotal(cart) + deliveryShare + serviceShare).toFixed(2);
  };

  const calculateGroupTotal = (): string => {
    const groupTotal = groupMembers.reduce((total, member) => total + calculateTotal(member.cart), 0);
    const userTotal = calculateTotal(userCart);
    return (groupTotal + userTotal + DELIVERY_FEE + SERVICE_FEE).toFixed(2);
  };

  const handleTopUp = () => {
    const amount = parseFloat(topUpAmount);
    if (isNaN(amount) || amount <= 0) {
      Alert.alert('Invalid Amount', 'Please enter a valid amount to top up.');
      return;
    }
    setWalletBalance((prevBalance) => prevBalance + amount);
    setTopUpAmount('');
    Alert.alert('Top-Up Successful', `Your wallet balance is now £${(walletBalance + amount).toFixed(2)}`);
  };

  const handleCheckout = () => {
    const total = parseFloat(calculateMemberTotal(userCart));
    if (walletBalance >= total) {
      setWalletBalance((prevBalance) => prevBalance - total);
      Alert.alert('Checkout Successful', `£${total.toFixed(2)} has been deducted from your wallet.`);
      setUserCart([]); 
      AsyncStorage.removeItem('userCart'); 
    } else {
      Alert.alert('Insufficient Balance', `You need £${(total - walletBalance).toFixed(2)} more to complete the purchase.`);
    }
  };

  return (
    <View style={styles.safeArea}>
      <ScrollView style={styles.scrollContent} contentContainerStyle={{ paddingBottom: 100 }}>
      <Text style={styles.headerText}>Group Checkout</Text>
        <View style={styles.walletContainer}>
          <Text style={styles.walletBalance}>Wallet Balance: £{walletBalance.toFixed(2)}</Text>
          <TextInput
            style={styles.input}
            placeholder="Enter amount to top up"
            value={topUpAmount}
            keyboardType="numeric"
            onChangeText={setTopUpAmount}/>
          <TouchableOpacity style={styles.topUpButton} onPress={handleTopUp}>
            <Text style={styles.topUpButtonText}>Top Up Wallet</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.memberContainer}>
          <Text style={styles.memberName}>Your Cart</Text>
          {userCart.length > 0 ? (
            userCart.map((product, index) => (
              <Text key={index} style={styles.productText}>
                {product.name} - £{product.price.toFixed(2)}
              </Text>
            ))
          ) : (
            <Text style={styles.emptyCartText}>Your cart is empty.</Text>
          )}
          <Text style={styles.totalText}>Your Total: £{calculateMemberTotal(userCart)}</Text>
        </View>
        {groupMembers.map((member, index) => (
          <View key={index} style={styles.memberContainer}>
            <Text style={styles.memberName}>{member.name}'s Cart</Text>
            {member.cart.map((product, i) => (
              <Text key={i} style={styles.productText}>
                {product.name} - £{product.price.toFixed(2)}
              </Text>
            ))}
            <Text style={styles.totalText}>Total: £{calculateMemberTotal(member.cart)}</Text>
          </View>
        ))}
        <View style={styles.summaryContainer}>
          <Text style={styles.summaryText}>Delivery Fee: £{DELIVERY_FEE.toFixed(2)}</Text>
          <Text style={styles.summaryText}>Service Fee: £{SERVICE_FEE.toFixed(2)}</Text>
          <Text style={styles.summaryTotal}>Group Total: £{calculateGroupTotal()}</Text>
        </View>
        <View style={styles.checkoutButtonContainer}>
          <TouchableOpacity style={styles.checkoutButton} onPress={handleCheckout}>
            <Text style={styles.checkoutButtonText}>Checkout</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: 'white',
  },
  scrollContent: {
    padding: 16,
    flexGrow: 1,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 16,
  },
  walletContainer: {
    padding: 16,
    backgroundColor: 'white',
    borderRadius: 8,
    marginBottom: 16,
  },
  walletBalance: {
    fontSize: 18,
    marginBottom: 8,
  },
  input: {
    borderWidth: 1,
    borderColor: 'grey',
    padding: 8,
    borderRadius: 4,
    marginBottom: 8,
  },
  topUpButton: {
    backgroundColor: 'green',
    padding: 10,
    borderRadius: 4,
    alignItems: 'center',
  },
  topUpButtonText: {
    color: 'white',
    fontSize: 16,
  },
  memberContainer: {
    backgroundColor: 'white',
    padding: 16,
    borderRadius: 8,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: 'lightgrey',
  },
  memberName: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  productText: {
    fontSize: 14,
    marginBottom: 4,
  },
  emptyCartText: {
    fontSize: 16,
    color: 'grey',
    fontStyle: 'italic',
    textAlign: 'center',
  },
  totalText: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 8,
  },
  summaryContainer: {
    padding: 16,
    backgroundColor: 'lightgrey',
    borderRadius: 8,
    marginBottom: 16,
  },
  summaryText: {
    fontSize: 14,
    marginBottom: 4,
  },
  summaryTotal: {
    fontSize: 18,
    fontWeight: 'bold',
    marginTop: 8,
  },
  checkoutButtonContainer: {
    padding: 16,
    backgroundColor: 'white',
    borderTopWidth: 1,
    borderColor: 'lightgrey',
  },
  checkoutButton: {
    backgroundColor: 'blue',
    padding: 16,
    borderRadius: 8,
    alignItems: 'center',
  },
  checkoutButtonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
