import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Alert } from 'react-native';
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

  useEffect(() => {
    axios
      .get<Product[]>('http://10.115.206.210:8000/products')
      .then((response) => {
        setProducts(response.data);
        generateGroupMembers(response.data);
      })
      .catch(() => Alert.alert('Error', 'Failed to load products.'));
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

  const addToUserCart = (product: Product) => {
    setUserCart((prevCart) => [...prevCart, product]);
    Alert.alert('Added to Cart', `${product.name} has been added to your cart.`);
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

  return (
    <View style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <Text style={styles.headerText}>Group Checkout</Text>
        <View style={styles.memberContainer}>
          <Text style={styles.memberName}>Your Cart</Text>
          {userCart.map((product, index) => (
            <Text key={index} style={styles.productText}>
              {product.name} - £{product.price.toFixed(2)}
            </Text>
          ))}
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
        <TouchableOpacity
          style={styles.checkoutButton}
          onPress={() =>
            Alert.alert('Checkout Successful', `Total Cost: £${calculateGroupTotal()}`)
          }>
          <Text style={styles.checkoutButtonText}>Checkout</Text>
        </TouchableOpacity>
      </View>
      </ScrollView >
    </View>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#f9f9f9',
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
  memberContainer: {
    backgroundColor: '#ffffff',
    padding: 16,
    borderRadius: 8,
    marginBottom: 16,
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
  totalText: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 8,
  },
  summaryContainer: {
    padding: 16,
    backgroundColor: '#e0e0e0',
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
    backgroundColor: '#f9f9f9',
    borderTopWidth: 1,
    borderColor: '#ccc',
  },
  checkoutButton: {
    backgroundColor: '#1d3d47',
    padding: 16,
    borderRadius: 8,
    alignItems: 'center',
  },
  checkoutButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
