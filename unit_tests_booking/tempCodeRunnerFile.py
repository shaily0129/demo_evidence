    def test_valid_request_with_large_age_value(self):
            response = self.post_request(
                {"request_id": "s222", "params": {"name": "Jacob", "country": "Canada", "age": "99"}}
            )
            self.assertEqual(response.status_code, 200)
            data = response.json()
            
            if data["complete"]:
                self.assertIsNotNone(data["booking_id"])  # Ensure booking_id is not None if complete
            else:
                self.assertIsNone(data["booking_id"])  # Ensure booking_id is None if not complete
            
            self.assertIsNone(data.get("interactions"))  # Ensure no interactions are present